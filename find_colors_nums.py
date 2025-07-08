from colour import Color
def colors_processing(text):
    colors = []
    for word in text.split():
        try:
            if Color(word):
                colors.append(word.lower())
        except ValueError:
            continue
    return colors

def num_processing(text):
    nums = []
    for num in text.split():
        if num.isdigit():
            nums.append(num)
    return nums