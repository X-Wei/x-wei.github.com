Title: [Android Dev] 1.4 Intents  
Date: 2017-02-07  
Slug:  andev_p1e4_intents  
Tags: android    
Series: Associate Android Developer Fast Track 
 
[TOC]


So far: single screen with a single activity. 

start activity from another activity: use ``Intent``s. 

Explicit intent: start a new activity
-------------------------------------
toy app: type some text, press button, and a new activity will appear with the typed words.

create activity in android studio: new → activity

call ``startActivity`` with an intent as parameter. 

Explicit intent constructor: a context (every ``Acitivity`` is a ``Context``), and a destination activity class. 

    Intent ineten = new Intent(MainActivity.this, ChildActivity.class);
    startActivity(intent);

This is called **explicit** intent as we know exactly which activity to start. 

in AndroidManifest.xml file, configure child activity having a back buttom to return to parent activity: 

    <activity
        android:name=".MainActivity"
        android:label="@string/app_name">
        <intent-filter>
            <action android:name="android.intent.action.MAIN" />

            <category android:name="android.intent.category.LAUNCHER" />
        </intent-filter>
    </activity>
    <!-- TODO (4) Configure DetailActivity's up button functionality -->
    <activity
        android:name=".DetailActivity"
        android:parentActivityName=".MainActivity">
        <meta-data
            android:name="android.suport.PARENT_ACTIVITY"
            android:value=".MainActivity" />
    </activity>


Passing data between activities
-------------------------------
in main activity: 
``Intent.putExtra(String name, String value)``
put data (*k-v pairs*) into the intent (some constant string names exists in Intent class, like ``Intent.EXTRA_TEXT``)
then start new activity with this intent. 

in child activity: 
use ``getIntent()`` to get the comming intent, then use ``intent.getStringExtra(String name)``, 
before getting extra data: use ``intent.hasExtra(name)`` to check if the extra stuff exists. 

    Intent commingIntent = getIntent();
    if(commingIntent.hasExtra(Intent.EXTRA_TEXT)){
        String txt = commingIntent.getStringExtra(Intent.EXTRA_TEXT);
        mDisplayText.setText(txt);
    }


Implicit Intent: opening a link
-------------------------------
when don't know/care which activity to start. 
example: want to visit a link or dial a number. 

ref of common intents: <https://developer.android.com/guide/components/intents-common.html>

most implicit intent contains 2 parameters: an action and the associated data (``Uri``). Or use ``intent.setData`` to add uri to intent. 
To test if there is any application that can handle the intent: use ``intent.resolveActivity(getPackageManager())``

    private void openWebPage(String url) {
        // TODO (2) Use Uri.parse to parse the String into a Uri
        Uri uri = Uri.parse(url);
        // TODO (3) Create an Intent with Intent.ACTION_VIEW and the webpage Uri as parameters
        Intent intent = new Intent(Intent.ACTION_VIEW, uri);
        // TODO (4) Verify that this Intent can be launched and then call startActivity
        if(intent.resolveActivity(getPackageManager()) != null){
            startActivity(intent);
        }
    }


URIs
----

**URI**: uniform resource identifier, a string that identifies resources. 

full format of an URI: 
![](../images/andev_p1e4_intents/pasted_image.png)

components: 

* scheme: ex. ``geo, http``...
* host
* path
* query
* fragment


example of URI: 

    uri1 = https://archive.org/web
    uri2 = geo:0,0?q=Montreal,Canada


construct a geo URI
-------------------
now: want to open a location on maps. 

<https://developers.google.com/maps/documentation/android-api/intents>

Use ``Uri.Builder`` to create complex URIs. 

    public void onClickOpenAddressButton(View v) {
            String address = "Boulvard des Marechaux";
            // TODO (6) Use Uri.Builder with the appropriate scheme and query to form the Uri for the address
            Uri.Builder builder = new Uri.Builder();
            builder.scheme("geo").path("0,0").query(address);
            Uri uri = builder.build();
            showMap(uri); // constructs an intent and starts activity
        }

Share Intent
------------

When mutilple apps that can handle this intent ⇒ a chooser will pop up. 
Example: open an image / share a piece of text / share link ... 
 → ``ShareCompat.IntentBuilder``  gives helper functionality for sharing data between activities.
Media type (MIME):
format: ``toplevel_type_name/subtype_name[; parameters]``
example: ``text/html;charset=UTF-8, image/png``, ``text/plain``, ``text/rtf, video/mp4``,...

    private void shareText(String txt) {
            String mimeType = "text/plain";
            String title = "title of chooser window";
            ShareCompat.IntentBuilder.from(this)
                    .setType(mimeType)
                    .setChooserTitle(title)
                    .setText(txt).startChooser();
        }

