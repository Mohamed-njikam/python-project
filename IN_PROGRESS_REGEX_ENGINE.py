import sys

sys.setrecursionlimit(10000)


def regex_check(reg, char):
    return reg == "" or reg == char or reg == "."


def regex_with_inter(pattern, chrs):
    index_ = pattern.index('?')
    index_word_after = index_ + 1
    index_word_before = index_ - 1
    return dif_regex_string(pattern[:index_] + pattern[index_word_after:], chrs) or \
           dif_regex_string(pattern[:index_word_before] + pattern[index_word_after:], chrs)


def regex_with_star(patter, charas):
    if patter[patter.index('*') - 1] not in charas:
        return dif_regex_string(patter[patter.index('*') + 1:], charas)
    elif patter[patter.index('*') - 1] in charas:
        if patter[patter.index('*') - 1] == charas[0]:
            return True
        else:
            return regex_with_star(patter, charas[1:])


def regex_with_plus(pat, ch):
    index_plus = pat.index('+')
    char_before = pat[index_plus - 1]
    if char_before == ".":
        return True
    elif char_before not in ch:
        return False
    elif char_before in ch:
        return compare_regex_string(pat[:index_plus] + pat[index_plus + 1:], ch)


def regex_escape(patt, str_):
    if str(patt).count('\\') < 2:
        escape_index = patt.index('\\')
        if patt[escape_index + 1] in ('?', '*', '+', '.', '^', '$'):
            return dif_regex_str_(patt[:escape_index] + patt[escape_index + 1:], str_)
    else:
        escape_index = patt.index('\\')
        if patt[escape_index + 1] == '\\':
            return dif_regex_str_(patt[:escape_index] + patt[escape_index + 1:], str_)


def dif_regex_str_(r, c):
    if len(r) == len(c) and '*' not in r and '+' not in r and '?' not in r:
        return compare_regex_string(r, c)
    else:
        if r == "." or r == c[:len(r)]:
            return True
        elif len(c) == 0:
            return False
        elif len(r) < len(c):
            if not compare_regex_string(r, c[:len(r)]):
                return dif_regex_string(r, c[1:])
            else:
                return True
        elif len(r) > len(c):
            if str(r).startswith('^') and not str(r).endswith('$'):
                return str(c).startswith(r[1:])
            elif str(r).endswith('$') and not str(r).startswith('^'):
                return str(c).endswith(r[:len(r) - 1])
            elif str(r).startswith('^') and str(r).endswith('$'):
                return str(c).startswith(r[1:len(r) - 1]) and str(c).endswith(r[1:len(r) - 1])
        return False


def compare_regex_string(regx, chars):
    if len(regx) == 0:
        return True
    elif len(chars) == 0:
        return False
    elif str(regx).startswith('^') and not str(regx).endswith('$'):
        return str(chars).startswith(regx[1:])
    elif str(regx).endswith('$') and not str(regx).startswith('^'):
        return str(chars).endswith(regx[:len(regx) - 1]) or regx[-2] == "."
    elif not regex_check(regx[0], chars[0]):
        return False
    elif len(regx) >= 2 and len(chars) >= 2:
        return compare_regex_string(regx[1:], chars[1:])
    else:
        return True


def dif_regex_string(rege, chara):
    if '\\' in rege:
        return regex_escape(rege, chara)
    if len(rege) == len(chara) and '*' not in rege and '+' not in rege and '?' not in rege:
        return compare_regex_string(rege, chara)
    else:
        if '+' in rege:
            return regex_with_plus(rege, chara)
        if '*' in rege:
            return regex_with_star(rege, chara)
        elif '?' in rege:
            return regex_with_inter(rege, chara)
        elif rege == "." or rege == chara[:len(rege)]:
            return True
        elif len(chara) == 0:
            return False
        elif len(rege) < len(chara):
            if not compare_regex_string(rege, chara[:len(rege)]):
                return dif_regex_string(rege, chara[1:])
            else:
                return True
        elif len(rege) > len(chara):
            if str(rege).startswith('^') and not str(rege).endswith('$'):
                return str(chara).startswith(rege[1:])
            elif str(rege).endswith('$') and not str(rege).startswith('^'):
                return str(chara).endswith(rege[:len(rege) - 1])
            elif str(rege).startswith('^') and str(rege).endswith('$'):
                return str(chara).startswith(rege[1:len(rege) - 1]) and str(chara).endswith(rege[1:len(rege) - 1])


regex, character = input().split("|")
print(dif_regex_string(regex, character))
