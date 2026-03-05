# beerfyi — Python Beer Encyclopedia Demo
Output demo.gif

Set FontSize 14
Set Width 920
Set Height 620
Set Shell "zsh"
Set Theme "Catppuccin Mocha"
Set TypingSpeed 35ms
Set Padding 20

Type `curl -s 'https://beerfyi.com/api/search/?q=IPA' | jq '.results[:3][] | {name, type}'`
Enter
Sleep 3s

Type `curl -s 'https://beerfyi.com/api/style/american-ipa/' | jq '{name, category, abv_range}'`
Enter
Sleep 3s

Type `curl -s 'https://beerfyi.com/api/random/' | jq '{name, category}'`
Enter
Sleep 3s

Sleep 2s
