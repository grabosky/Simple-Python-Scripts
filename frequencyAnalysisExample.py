#Adam Grabowski; ChatGPT-3
#2023-12-16
#Statistical analysis - Character frequency analysis of a sample data. Show plot in pyplot. 
#Sample data is "Lorem ipsum" text

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
    example_string = Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur pretium tempor ultricies. In hac habitasse platea dictumst. Curabitur consequat felis nec nisi aliquam, et tincidunt ante luctus. Cras a suscipit mi. Nam ac aliquam velit. Duis vitae nulla venenatis, fermentum neque a, porta mauris. Aenean nec ligula non elit dictum tristique.

Nullam fermentum efficitur cursus. Fusce egestas mi non nulla semper porttitor. Duis blandit feugiat lacus bibendum sodales. Curabitur ut lorem scelerisque, pellentesque lectus eget, varius magna. Nulla tempor augue in imperdiet maximus. Sed posuere, tortor ac dignissim commodo, ipsum tellus volutpat lorem, et sagittis neque mauris ac risus. Vivamus ultricies imperdiet orci. Mauris quam nisl, ultrices nec fermentum quis, auctor ut elit.

Nullam eget congue magna. Donec hendrerit venenatis sapien a sagittis. Nullam consectetur purus leo, et pulvinar orci porttitor at. Vestibulum molestie id ipsum pulvinar ornare. Donec gravida congue diam elementum fringilla. Maecenas ac molestie lectus. Sed congue vel ante ut vulputate. Suspendisse sagittis nulla eu lectus efficitur viverra. Mauris metus dui, sollicitudin non pretium quis, varius eu lorem. Maecenas a bibendum lectus, sollicitudin dictum elit. Nulla eget consequat justo. Cras tristique suscipit quam, id gravida magna tempor nec. Proin magna dui, vulputate at commodo in, sodales nec massa. Aliquam congue, magna ac accumsan elementum, ligula augue tristique erat, ut accumsan lectus metus non libero.

Maecenas tristique risus imperdiet dolor commodo iaculis. Mauris tortor odio, tempus at gravida sit amet, dapibus sed risus. Aliquam egestas in felis vel pulvinar. In hac habitasse platea dictumst. Duis maximus ultrices venenatis. Ut rutrum ornare nisi ac lobortis. Nam congue, nunc eget egestas volutpat, eros nulla sollicitudin metus, non sollicitudin tortor risus accumsan mi. Curabitur viverra, purus vel volutpat pharetra, leo ante venenatis risus, ac malesuada est erat eu sapien. Vivamus convallis, felis fringilla imperdiet ultricies, odio tellus ultrices nisi, sed pretium nunc mauris non dolor. Duis in facilisis erat, et vulputate leo. Duis pharetra dapibus magna. Cras sollicitudin dolor id dignissim venenatis. Etiam ultricies volutpat nisl nec tempus. Sed eleifend vestibulum lacinia. Phasellus sagittis mauris et velit interdum, et maximus lacus mollis. Aliquam eu tellus egestas odio tincidunt sodales at sit amet ligula.

Cras est nulla, mollis eget felis vel, condimentum dapibus arcu. Curabitur nunc augue, congue ut libero at, luctus feugiat purus. Sed dui tortor, tincidunt pellentesque felis vitae, placerat placerat turpis. Vestibulum suscipit euismod dui commodo pharetra. Nunc eget nunc id magna dapibus varius. Vestibulum vulputate sem ac lacinia volutpat. In tellus nisi, hendrerit nec magna id, hendrerit pellentesque ipsum. Nam commodo, felis tristique malesuada porttitor, metus felis ornare dui, ut ullamcorper libero nisl eu arcu. Curabitur sed eros elementum lorem faucibus dapibus et ac augue. Phasellus vitae facilisis dui. Sed elementum sed nulla in gravida. In hac habitasse platea dictumst. Etiam dictum tortor non facilisis lacinia."

    characters, frequencies = frequency_analysis(example_string)

    # Display the character frequency analysis
    plot_frequency_analysis(characters, frequencies)
