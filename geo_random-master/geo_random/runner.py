import sys
from geo_random.console import COMMANDS


if __name__ == '__main__':
    mode = sys.argv[1]

    if mode not in COMMANDS:
        raise Exception('Undefined mode')

    run_args = sys.argv[2:]
    mode_cls = COMMANDS[mode]
    mode_obj = mode_cls(run_args)

    result = mode_obj.run()
    print('Result: {}'.format(result))
