import wikipedia
import argparse
from colorama import init, Back, Fore


init(autoreset=True)


parser = argparse.ArgumentParser(description='Lightweight console Wikipedia API interpreter')
parser.add_argument('query', type=str, help="Search query")
parser.add_argument('-lg', '--language', type=str, help="Wikipedia language")
parser.add_argument('-o', '--output', type=str, help="Redirecting output to specified file")
args=parser.parse_args()


wikipedia.set_lang(args.language)
res=wikipedia.page(args.query)
if args.output:
    with open(args.output, "a") as op:
        op.write(res.content)
        op.close()
print(Fore.CYAN + res.title)
print(Fore.YELLOW + "= = = = = =\n", res.content)
