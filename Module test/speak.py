from gtts import gTTS
from playsound import playsound

a= '''I love it when you call me señorita
I wish I could pretend I didn't need ya
But every touch is ooh, la-la-la
It's true, la-la-la
Ooh, I should be running
Ooh, you keep me coming for ya
Land in Miami
The air was hot from summer rain
Sweat dripping off me
Before I even knew her name, la-la-la
It felt like ooh, la-la-la
Yeah, no
Sapphire moonlight
We danced for hours in the sand
Tequila Sunrise
Her body fit right in my hands, la-la-la
It felt like ooh, la-la-la, yeah
I love it when you call me señorita
I wish I could pretend I didn't need ya
But every touch is ooh, la-la-la
It's true, la-la-la
Ooh, I should be running
Ooh, you know I love it when you call me señorita
I wish it wasn't so damn hard to leave ya
But every touch is ooh, la-la-la
It's true, la-la-la
Ooh, I should be running
Ooh, you keep me coming for ya'''

tts = gTTS(a, lang='en')
tts.save("hello.mp3")
playsound("hello.mp3")
