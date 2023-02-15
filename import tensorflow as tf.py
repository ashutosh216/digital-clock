segments = {0:['###','# #','# #','# #','###'],
            1:['  #','  #','  #','  #','  #'],
            2:['###','  #','###','#  ','###'],
            3:['###','  #','###','  #','###'],
            4:['# #','# #','###','  #','  #'],
            5:['###','#  ','###','  #','###'],
            6:['###','#  ','###','# #','###'],
            7:['###','  #','  #','  #','  #'],
            8:['###','# #','###','# #','###'],
            9:['###','# #','###','  #','###']
            }


def segment_helper(number: str):
    out = ["","", "", "", ""]
    try:
        for digit in number:
            for i, line in enumerate(segments[int(digit)], 0):
                out[i] += ("  "+line if out else line)
        return "\n".join(out)
    except KeyError:
        return "Invalid number"
    except ValueError:
        return "Invalid number"


print(segment_helper("12345678910111213"))