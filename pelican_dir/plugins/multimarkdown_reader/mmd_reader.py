import subprocess
from pelican import signals
from pelican.readers import BaseReader
from pelican.utils import pelican_open

class MmdReader(BaseReader):
    enabled = True
    file_extensions = ['md', 'markdown', 'mkd', 'mdown']

    def read(self, filename):
        with pelican_open(filename) as fp:
            text = list(fp.splitlines())

        metadata = {}
        for i, line in enumerate(text):
            kv = line.split(':', 1)
            if len(kv) == 2:
                name, value = kv[0].lower(), kv[1].strip()
                metadata[name] = self.process_metadata(name, value)
            else:
                content = "\n".join(text[i:])
                break

        mmd_cmd = ["multimarkdown"]

        proc = subprocess.Popen(mmd_cmd,
                                stdin = subprocess.PIPE,
                                stdout = subprocess.PIPE)

        output = proc.communicate(content.encode('utf-8'))[0].decode('utf-8')
        status = proc.wait()
        if status:
            raise subprocess.CalledProcessError(status, mmd_cmd)

        return output, metadata

def add_reader(readers):
    for ext in MmdReader.file_extensions:
        readers.reader_classes[ext] = MmdReader

def register():
    signals.readers_init.connect(add_reader)
