def color_print(text, color='Simple'):
    COLORS = {
        'grey': '30',
        'orange': '31',
        'yellow': '33',
        'blue': '32',
        'purple': '35',

    }
    """Prints the colorful values to a stream, or to sys.stdout by default.

    text
        text that you want to print.
    color
      write color name that you want to put on your text.
      {[color for color in COLORS]}.
    """
    
    if color.lower() not in COLORS:
        print(text)
        return 

    print(f'\033[1;{COLORS[color]}m' + text + '\033[0m')
    return