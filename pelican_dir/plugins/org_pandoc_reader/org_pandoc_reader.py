import subprocess
import re
from pelican import signals
from pelican.readers import BaseReader
from pelican.utils import pelican_open

class OrgPandocReader(BaseReader):
    enabled = True
    file_extensions = ['org']

    def read(self, filename):
        with pelican_open(filename) as fp:
            text = list(fp.splitlines())

        metadata = {}
        for i, line in enumerate(text):
            meta_match = re.match(r'^#\+([a-zA-Z]+):(.*)', line)
            if meta_match:
                name = meta_match.group(1).lower()
                value = meta_match.group(2).strip()
                metadata[name] = self.process_metadata(name, value)
            else:
                content = "\n".join(text[i:])
                break

        extra_args = self.settings.get('ORG_PANDOC_ARGS', [])
        extensions = self.settings.get('ORG_PANDOC_EXTENSIONS', '')
        if isinstance(extensions, list):
            extensions = ''.join(extensions)

        pandoc_cmd = ["pandoc", "--from=org" + extensions, "--to=html5"]
        pandoc_cmd.extend(extra_args)

        proc = subprocess.Popen(pandoc_cmd,
                                stdin = subprocess.PIPE,
                                stdout = subprocess.PIPE)

        output = proc.communicate(content.encode('utf-8'))[0].decode('utf-8')
        status = proc.wait()
        if status:
            raise subprocess.CalledProcessError(status, pandoc_cmd)

        return output, metadata

def add_reader(readers):
    for ext in OrgPandocReader.file_extensions:
        readers.reader_classes[ext] = OrgPandocReader

def register():
    signals.readers_init.connect(add_reader)
