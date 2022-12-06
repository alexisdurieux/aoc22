from aoc22.parse import load

def find_marker_pos(signal: str, marker_len: int):
    for i in range(len(signal) - marker_len):
        if len(set(signal[i:i+marker_len])) == marker_len:
            return i + marker_len

if __name__ == "__main__":
    lines = load("inputs/6.txt")
    signal = lines[0]
    print(find_marker_pos("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14))
    res1 = find_marker_pos(signal, 4)
    print(res1)
    res2 = find_marker_pos(signal, 14)
    print(res2)


     
