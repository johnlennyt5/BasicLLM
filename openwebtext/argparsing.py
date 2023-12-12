import argparse
def parse_args():
    parser = argparse.ArgumentParser(description='This is a demostration program.')

    # Here we add an argument to the parser, specifying the expected typw, a help message.. etc 
    parser.add_argument('-bs', type=str, required=True, help='please provde a batch_size')

    return parser.parse_args()

def main():
    args = parse_args()
    
    # Now we can use the argument value in our program
    print(f'btach_size: {args.bs}')

if __name__ == '__main__':
    main()