import os

def replace_eyes(line):
    """Replaces '0   0' with '-' or '👁   👁'."""
    return line.replace('0   0', '-').replace('👁   👁', '-')

def process_file(input_file, output_dir):
    """Processes an input file and creates the corresponding output file."""
    output_file = os.path.join(output_dir, os.path.basename(input_file).replace('.in', 'Closed.out'))
    with open(input_file, 'r') as f_in, open(output_file, 'w',encoding='utf-8') as f_out:
        for line in f_in:
            f_out.write(replace_eyes(line))

def main():
    input_dir = 'pictures'
    output_dir = os.path.join('closealleyes', 'picturesclosed')
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Process each input file
    for filename in os.listdir(input_dir):
        if filename.endswith('.in'):
            input_file = os.path.join(input_dir, filename)
            process_file(input_file, output_dir)
            print(f"Processed {filename}")

if __name__ == "__main__":
    main()
