def does_arg_allow_row(row, arg):
    # todo remove special characters
    arg_key, arg_value = arg
    if arg_key.endswith('_at_least'):
        key_without_suffix = arg_key[:-len('_at_least')]
        return float(row[key_without_suffix]) >= float(arg_value)

    if arg_key.endswith('_at_most'):
        key_without_suffix = arg_key[:-len('_at_most')]
        return float(row[key_without_suffix]) <= float(arg_value)

    if arg_key == 'overview_simple':
        # naive implementation that needs optimization
        overview = row['overview'].lower()
        return arg_value in overview

    if arg_key == 'overview':
        # naive implementation that needs optimization
        overview = row[arg_key].lower()
        return any([any([word == ov for ov in overview.split(' ')]) for word in arg_value.split(' ')])

    if arg_key == 'title_exact':
        return row['title'].lower() == arg_value.lower()

    if arg_key == 'title':
        return arg_value.lower() in row['title'].lower()

    return row[arg_key].lower() == arg_value.lower()


def do_args_allow_row(row, args):
    return all([does_arg_allow_row(row, arg) for arg in args.items()])


def count_total_words_in_ref(ref_words, words):
    return sum([ref in words.split(' ') for ref in ref_words.split(' ')])