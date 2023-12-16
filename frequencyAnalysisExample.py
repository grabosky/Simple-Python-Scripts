#Adam Grabowski; ChatGPT-3
#2023-12-16
#Statistical analysis - Character frequency analysis of a sample data. Show plot in pyplot. 
#Sample data was created by another script to print a long list of random characters a-b, A-B, special chars ie. !@#$%^&*, and a random number 0-9 every 6th char. 

from collections import Counter
import matplotlib.pyplot as plt

def frequency_analysis(data):
    # Count the frequency of each character
    char_freq = Counter(data)

    # Sort characters by frequency in descending order
    sorted_chars = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)

    # Separate characters and their frequencies
    characters, frequencies = zip(*sorted_chars)

    return characters, frequencies

def plot_frequency_analysis(characters, frequencies):
    plt.bar(characters, frequencies)
    plt.xlabel('Characters')
    plt.ylabel('Frequency')
    plt.title('Character Frequency Analysis')
    plt.show()

if __name__ == '__main__':
    # The provided example string
    example_string = "5d$Cg@4hFciG8@J!=j2**=^d9h@-dC6@&a&-5I^i@=6IIi=E9B#A^G7@e=-c4F#Ba@9fBCHE1&A!&I7eJ#IC1B+g@G4aag!H3Ed& $f7cCEfH5C##E!9-$!BF7gIafB8#-BI$6BGba!7CDEa+7&g@=a1J+GH*3#@@&f2+C#J$5C-=jG3G$*#h9d+J+*8FjFHe4aD&c&9g !#Bc2&A&fG5*j*ed7d+==H7Jid&d1ig#gD1DFa$-7CI#ef1B!Bff8!J&fg1GAB+$9&=a^D7IjBh+4jI&$G6^hEj$5!#HD&1!^*&i 6!A+!G7Ef*-a2BI#Ij8ij=Ig4!JA@G6GgGiI5E-eD#1c#@&J8cj#^*7$B=@d6@#=gF7Heejf6@&#-h6h$hbB3-DJG^1$-dbE9JdA EE7*!IA&3j-bf+8=H-$g4CBd+B8c$dd=4#DjH=3jdIFG7!Ggf=8Gd*^C4eDI$D9-g@*&2idc-h8IjdA@8d@JH&4EJa@*4@hd^a2B H&d+1E=dI$7cGCGe4$d-Hf1h=Ff@6D&C+A3@ig+i9hCd*i9$F@cj4j#gAG7H&B+d9&+@ja9F+Gah7dFIh^2+*D$!6BfIgc2+chb= 3&H-Ja6*=iiH7ggi+H7=J+cF6g-a#$6#+^gE6FCEe-4jb#aB4a^-GB7+hdc@2H*!+&5bEC*@7#cbfb9Edc^b9hjAGd9a-^Gj2D&G Ef7Dhf=#2H^fCI6a@Ged1@ia^g3bDAeE7!IJca4aDh^E3F$bE&6Hi$F^4&$iF+7=JFii6Af@-A1FDJbj6^djce5F#Gfa5fGiF-3d $Gai9=Eg+h2AfbgH5$+hbe6BHhhB2JJGDc5a=HIb1=b$$*7h@!aC5*=fGd9Jaa#1Db=@d2eGeDg9c!!&!6#&abF8JFee$5-bAFd 2-FGg@2!!^ag5i&gcc8I$&JI6*b=^c6ic&Db7AhI-G1^Ha#f3^$=@G5ecEDH1f$egA6fAC#E4jfifa9*I-Dj5d#Bbc3aEgHf3gIh cf1gg-DH5cF+!j6DFBFf8J=HBj4I^Ig@9d#H@J2jDCI&3eDC#i4Bh!@j4HI#Fe9G##*#4@CDba9Bjgc$9GAh!c9eJC*!2hfj$#5f *$fF1G=H*C4$@cjg5!I+@e3!F@f&2EF+B+3Iah+d5!+!j^2*@I$a1HJiic1H!DdJ3+*-jD2+ChdD7a#B!=9@Ici-7#+Ddg8jBD#f 4$*jE@4&G&DJ5@DBc&9jhjae5DC*@&6+^b+A8fbCDH6H&D=+1F&dcb2DBG!*4#jb=@7=JfFc1*GaIG2&IJ-&2^GeHd4Eh&!@1ce#"

    characters, frequencies = frequency_analysis(example_string)

    # Display the character frequency analysis
    plot_frequency_analysis(characters, frequencies)
