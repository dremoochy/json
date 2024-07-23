from argparse import *
import json
parser = ArgumentParser(
                    prog='jc',
                    description='json creator',
                    epilog='Coded by gtihub.com/dremoochy')
parser.add_argument('directory')
parser.add_argument('filename')
parser.add_argument('-c','--contents',type=str,required=False)
args = parser.parse_args()
try : 
    print(f'Writing {args.contents} to {args.filename} in {args.directory}') if args.contents is not None else print(f'Inflating {args.filename} at {args.directory}')
    with open(fr'{args.directory}\{args.filename}.json','w') as f:
        json.dump(json.loads(args.contents),f) if args.contents is not None else f.write('//empty')
    f.close()
    print('Success!')
except :
    print('Wild error encountered!')