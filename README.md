# CAPTCHA-Audio-Bypass
This repository contains a Proof-of-Concept (PoC) script to demonstrate how CAPTCHA's can be bypassed by exploiting accessibility features. Specifically, in this case, the script bypasses reCAPTCHAv2, by exploiting alternative puzzles for the visually impaired.

# The Exploit
reCAPTCHA has an audio challenge option for the visually impaired.  By selecting the "headphones" icon at the bottom of the reCAPTCHA challenge, you can opt to do the audio challenge instead of the visual puzzle.

![reCAPTCHA](https://1.bp.blogspot.com/-6LMsicgvSZE/XslybG_kLGI/AAAAAAAACvk/HKyjDqXi-xwRWItrPBRfMgkMBAfc_RVGwCPcBGAYYCw/s400/Screen%2BShot%2B2020-05-23%2Bat%2B1.54.23%2BPM.png)

This exploit example uses Google's Speech Recognition API to exploit this functionality, by taking the following steps:
1. Click the "I'm not a robot" checkbox
2. Upon being prompted to solve the challenge...click the Audio Challenge button at the bottom
3. Click the "Play" button to start the audio
4. Begin a short (5 second) local recording, to capture the audio in a WAV file
5. Immediately send that wave file up to the Google speech recognition platform for analysis
6. Once returned, supply the interpreted text to the input field and click "Verify"
7. Hope that Google's speech recognition software is stronger than their reCAPTCHA software :)

The test was run on Google's publicly available reCAPTCHAv2 demo (https://www.google.com/recaptcha/api2/demo).

[![CAPTCHA Bypass POC](https://img.youtube.com/vi/WbraHJ9GJO4/0.jpg)](https://www.youtube.com/watch?v=WbraHJ9GJO4 "CAPTCHA Bypass POC")

This exploit is a very basic proof-of-concept that requires that the graphical elements correspond to desktop coordinates. This was done intentionally to demonstrate the risk potential, while simultaneously minimizing the likelihood that the script could easily be misused by script kiddies.  
