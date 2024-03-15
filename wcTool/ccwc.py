#!/usr/bin/env python3

import argparse
import os.path
import sys


def main():
    parser = create_argument_parser()
    args = parser.parse_args()
    input_source = args.input_source

    if isinstance(input_source, str):
        wc_for_file(args, input_source)
    else:
        wc_for_input_stream(args, input_source)


def wc_for_file(args, file_name):
    if not os.path.exists(file_name):
        print(f"Error: The file {file_name} does not exist.")
        return

    get_count(args, file_name)


def get_count(args, file_name):
    if args.c:
        print(f"Bytes: {count_bytes(file_name)} {file_name}")
    elif args.l:
        _, line_count = count_words_and_lines(file_name)
        print(f"Lines: {line_count} {file_name}")
    elif args.w:
        word_count, _ = count_words_and_lines(file_name)
        print(f"Words: {word_count} {file_name}")
    elif args.m:
        print(f"Characters: {count_characters(file_name)}")
    else:
        word_count, line_count = count_words_and_lines(file_name)
        print(f"{line_count} {word_count} {count_bytes(file_name)} {file_name}")


def wc_for_input_stream(args, input_stream):
    line_count, word_count, character_count, byte_count = get_count_for_input_stream(input_stream)

    if args.c:
        print(f"Bytes: {byte_count}")
    elif args.l:
        print(f"Lines: {line_count}")
    elif args.w:
        print(f"Word Count: {word_count}")
    elif args.m:
        print(f"Characters: {character_count}")


def get_count_for_input_stream(input_stream):
    line_count = 0
    word_count = 0
    byte_count = 0
    character_count = 0

    for line in input_stream:
        line_count += 1
        words = line.split()
        word_count += len(words)
        character_count += sum(len(word) for word in words)
        byte_count += len(line.encode())  # Counting bytes

    return line_count, word_count, character_count, byte_count


def create_argument_parser():
    parser = argparse.ArgumentParser(
        prog='ccwc',
        description='WC Tool',
        epilog='Created by Kara Ducasse')

    parser.add_argument('input_source', nargs='?', default=sys.stdin,
                        help='Description of filename argument')  # Positional arg
    parser.add_argument('-c', action='store_true', help='Outputs the number of bytes in a file')  # Optional arg
    parser.add_argument('-l', action='store_true', help='Outputs the number of lines in a file')  # Optional arg
    parser.add_argument('-w', action='store_true', help='Outputs the number of words in a file')  # Optional arg
    parser.add_argument('-m', action='store_true', help='Outputs the number of characters in a file')  # Optional arg

    return parser


def count_bytes(file_path):
    return os.path.getsize(file_path)


def count_words_and_lines(file_path):
    word_count = 0
    line_count = 0
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            word_count += len(line.strip().split())
            line_count += 1

    return word_count, line_count


def count_characters(file_path):
    character_count = 0

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            character_count += len(line)

    return character_count


main()
