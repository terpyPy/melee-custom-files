# dat file parser #
  YOU MUST EXPORT ALL YOUR DAT FILES TO TXT FILES, IT WILL NOT READ JASON, DAT, LAT, BAT OR RTF
  
                   *This script finds the offset addresses at which animation colors and more are located*
  1.First step to using datFileParser is to export the character files from HxD as .txt files NOT RTF YOU MUST CHANGE THE FILE FORMAT!!!!
  
  2.Then parse to identify the color code type (rgb,rrggbb, ect..) and store the offset address that hexset pattern is located in.
  
  3.Finally the script compares the found offsets with the list of known character animation/color offsets and the color code hex format.
  
        Also lists any other offset with hexsets that match its patterns, 
        but will not return them when filtering for known locations.
        I only have about 6-9 months of hobby coding and one python class, 
        this is not good code, i know its probably bad,
        but I’m loving this so much I’m going back to school.
        For either data science or software engineering
  
#  melee-custom-files  #
  files for custom melee textures and animations for from scrap projects or use my fully modded character dat files
  
            * may cause slippi desync i did my best to preserver file texture size and resolution *
                The ganon file with color changed down b might cause desync because unknowing, 
                I changed some of the lens flare to invalid screen locations.
                if to many of those particles are in invalid locations,
                while the hit box is still valid desync and weird shit happens.
  

##### How to know which file is what? #####
  Rainbow shine is the most worked on animation file, contains rainbow shine for Fox/Falco and the tip of Firefox is blue.

  PlFc is Falco’s animation file.

  EfFx is the shared animations between Fox and Falco (shine and Firefox).

  PlMs is Marths sword swing animation (also replaces the color of up B).

  EfCoData.dat is the shared animations for all characters along with PlCo.dat.

  dat file parser.exe is the original script i scrapped up after i read this post on,
  smashborads: https://smashboards.com/threads/changing-color-effects-in-melee.313177/
