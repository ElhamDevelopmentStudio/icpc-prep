def main():
    import sys
    input = """1
    xyx
    golago
    """ 
    ptr = 0
    test_cases = int(input[ptr].strip())
    ptr += 1
    
    for _ in range(test_cases):
        pattern = input[ptr].strip()
        ptr += 1
        s = input[ptr].strip()
        ptr += 1
        
        # Determine if we need to swap x and y in the pattern
        swap = False
        cx = pattern.count('x')
        cy = pattern.count('y')
        original_pattern = pattern
        
        if cx > 0 and cy > 0:
            if pattern[0] == 'y':
                # Swap x and y in the pattern
                swapped_pattern = []
                for c in pattern:
                    if c == 'x':
                        swapped_pattern.append('y')
                    else:
                        swapped_pattern.append('x')
                pattern = ''.join(swapped_pattern)
                swap = True
                cx, cy = cy, cx
        
        # Handle patterns with only x or only y
        if cy == 0:
            # Only x's in the pattern
            if len(s) % cx != 0:
                print('[]')
                continue
            x_len = len(s) // cx
            x_val = s[:x_len]
            valid = True
            for i in range(cx):
                start = i * x_len
                end = start + x_len
                if end > len(s) or s[start:end] != x_val:
                    valid = False
                    break
            if valid:
                if swap:
                    print(f'["", "{x_val}"]')
                else:
                    print(f'["{x_val}", ""]')
            else:
                print('[]')
            continue
        
        if cx == 0:
            # Only y's in the pattern
            if len(s) % cy != 0:
                print('[]')
                continue
            y_len = len(s) // cy
            y_val = s[:y_len]
            valid = True
            for i in range(cy):
                start = i * y_len
                end = start + y_len
                if end > len(s) or s[start:end] != y_val:
                    valid = False
                    break
            if valid:
                if swap:
                    print(f'["{y_val}", ""]')
                else:
                    print(f'["", "{y_val}"]')
            else:
                print('[]')
            continue
        
        # Handle patterns with both x and y
        len_s = len(s)
        max_x_len = (len_s - cy) // cx
        found = False
        result = []
        
        for x_len in range(1, max_x_len + 1):
            total_remaining = len_s - (cx * x_len)
            if total_remaining < cy * 1:
                continue
            if total_remaining % cy != 0:
                continue
            y_len = total_remaining // cy
            if y_len < 1:
                continue
            
            current_pos = 0
            x_val = s[current_pos:current_pos + x_len]
            current_pos += x_len
            y_val = None
            valid = True
            
            for c in pattern[1:]:
                if c == 'x':
                    if current_pos + x_len > len_s:
                        valid = False
                        break
                    substr = s[current_pos:current_pos + x_len]
                    if substr != x_val:
                        valid = False
                        break
                    current_pos += x_len
                else:
                    if current_pos + y_len > len_s:
                        valid = False
                        break
                    if y_val is None:
                        y_val = s[current_pos:current_pos + y_len]
                        current_pos += y_len
                    else:
                        substr = s[current_pos:current_pos + y_len]
                        if substr != y_val:
                            valid = False
                            break
                        current_pos += y_len
                if not valid:
                    break
            
            if valid and current_pos == len_s:
                if swap:
                    result = [y_val, x_val]
                else:
                    result = [x_val, y_val]
                found = True
                break
        
        if found:
            print(f'["{result[0]}", "{result[1]}"]')
        else:
            print('[]')

if __name__ == "__main__":
    main()
