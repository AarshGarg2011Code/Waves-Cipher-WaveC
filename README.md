# Waves Cipher (WaveC)
## When the seas try to keep secrets.
### The Waves Cipher is a discontinued project of mine which, by the name "Waves", uses wave patterns to obfuscate text.
I had initially started this project thinking *the patterns found in waves, is cool and can be used to displace characters by their encodings.*
*The project was discontinued* because well, *although diffusion made it impossible to tell what the original text was, the number of permutations of WaveC was very small*, like, SMALL (in thousands only), *making it way more vulnerable to attacks* of brute-force if the attacker knows the text was encrypted using WaveC.
#### But you all can make it better!
The purpose of why I am making this open source is, I want whoever is interested in this, to develop it, and make its permutations stronger and more in number...
##### How this primitive version of WaveC works (as of early September 2026):
This version has inbuilt presets for various wave patterns (including mathematically calculated ones based on divisibility and multiplication), the points of the waves of which are given Increase/Decrease Magnitudes based on how high they are from the central axis. For example, if a wave's amplitude is 5, the Increase and Decrease magnitudes for one full wave will be: ```0,1,2,3,4,5,4,3,2,1,0,-1,-2,-3,-4,-5,-4,-3,-2,-1,0```
The preset wave patterns include __FOE (Frequency based On Even characters), FDN (Frequency based on Divisible-by-N characters), DNI (Divisibility-by-N Increase), DND (Divisibility-by-N Decrease), SINEW (Sine Wave), SAWW (Sawtooth Wave), SQRW (Square Wave) and TRIW (Triangle Wave).
To see how these waves work, analyze ```waves.py``` and find the Python logics of each preset. To see ALL presets that are available (All versions of the ones mentioned above based on various numerical factors), view ```AllWaveConfigs.json```.
##### The amount of New Developments Possibilities for WaveC is HUGE!
There are many ways you all can develop this project further; here is a hint for one of them:
###### Random Seed Permutations: *You can make a system where Base62-Encoded strings of 20-30 digits affect the wave's shape and I/D Magnitudes!*
### This was all from me, Aarsh Garg, for this project, to whoever read the whole README, you can take this project forward.
###### ps. there is a helper python importable that can help you make ASCII-Character graphs of text. There is also a tester file. Good Luck!
