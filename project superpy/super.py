# Imports
import argparse
from date_function import reset_date, advance_time, change_date
from buy import buy
from sell import sell
from report import sold_today_total, sold_in_month, bought_in_month, \
    bought_today_total, profit_today, profit_in_month, report_inventory, \
    offer_products, report_sold, report_bought
from rich.console import Console
from rich.theme import Theme


custom_theme = Theme({'success': 'green', 'error': 'bold red'})
console = Console(theme=custom_theme)


# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# gevonden op stackoverflow om spatie van een lege metavar weg te halen
class SingleMetavarHelpFormatter(argparse.HelpFormatter):
    def _format_action_invocation(self, action):
        if not action.option_strings:
            metavar, = self._metavar_formatter(action, action.dest)(1)
            return metavar
        else:
            parts = []
            if action.nargs == 0:
                parts.extend(action.option_strings)
            else:
                default = action.dest.upper()
                args_string = self._format_args(action, default)
                parts.extend(action.option_strings)
                parts[-1] += ' %s' % args_string
            return ', '.join(parts)


# dictonairy van functions zoals in de les uitgelegd
func_dict = {
    'buy': buy,
    'sell': sell,
    'sold_today': sold_today_total,
    'bought_today': bought_today_total,
    'profit_today': profit_today,
    'bought_in_month': bought_in_month,
    'sold_in_month': sold_in_month,
    'profit_in_month': profit_in_month,
    'reset_date': reset_date,
    'advance_time': advance_time,
    'change_date': change_date,
    'report_inventory': report_inventory,
    'offer_products': offer_products,
    'report_sold': report_sold,
    'report_bought': report_bought
}
my_parser = argparse.ArgumentParser(prog='PROG',
                                    formatter_class=SingleMetavarHelpFormatter)
my_parser.add_argument('function', choices=list(func_dict.keys()),
                       type=str,
                       help='function to call')
my_parser.add_argument('-p', '--product_name',
                       help='product name',
                       metavar='')
my_parser.add_argument('-e', '--exp_date',
                       help='expiration date yyyy-mm-dd',
                       metavar='')
my_parser.add_argument('-b', '--buy_price',
                       type=float,
                       help='buy price',
                       metavar='')
my_parser.add_argument('-s', '--sell_price',
                       type=float,
                       help='sell price',
                       metavar='')
my_parser.add_argument('-y', '--year_month',
                       help='in format yyyy-mm',
                       metavar='')
my_parser.add_argument('-d', '--days',
                       type=int,
                       help='days to advance time with',
                       metavar='')
my_parser.add_argument('-a', '--date',
                       help='date format yyyy-mm-dd',
                       metavar='')


args = my_parser.parse_args()

# hier call ik al mijn functies
if args.function == 'buy':
    if args.product_name is None:
        print("required product name", style="error")
        exit()
    elif args.buy_price is None:
        print('required product price', style="error")
        exit()
    elif args.exp_date is None:
        print('required expiration date', style='error')
        exit()
    else:
        func_dict[args.function](
            args.product_name, args.buy_price, args.exp_date)

elif args.function == 'sell':
    if args.product_name is None:
        print('required product name', style="error")
        exit()
    elif args.sell_price is None:
        print('required product price', style="error")
        exit()
    func_dict[args.function](
        args.product_name, args.sell_price)

elif args.function == 'sold_today':
    func_dict[args.function]()

elif args.function == 'bought_today':
    func_dict[args.function]()

elif args.function == 'profit_today':
    func_dict[args.function]()

elif args.function == 'bought_in_month':
    if len(args.year_month) != 7:
        print('use format YYYY-MM', style="error")
        exit()
    elif args.year_month[4] != '-':
        print('use format YYYY-MM', style="error")
        exit()
    func_dict[args.function](args.year_month)

elif args.function == 'sold_in_month':
    if len(args.year_month) != 7:
        print('use format YYYY-MM', style="error")
        exit()
    elif args.year_month[4] != '-':
        print('use format YYYY-MM', style="error")
        exit()
    func_dict[args.function](args.year_month)

elif args.function == 'profit_in_month':
    if len(args.year_month) != 7:
        print('use format YYYY-MM', style="error")
        exit()
    elif args.year_month[4] != '-':
        print('use format YYYY-MM', style="error")
        exit()
    func_dict[args.function](args.year_month)

elif args.function == 'reset_date':
    func_dict[args.function]()

elif args.function == 'advance_time':
    func_dict[args.function](args.days)

elif args.function == 'change_date':
    func_dict[args.function](args.date)

elif args.function == 'report_inventory':
    func_dict[args.function]()

elif args.function == 'offer_products':
    func_dict[args.function]()

elif args.function == 'report_sold':
    func_dict[args.function]()

elif args.function == 'report_bought':
    func_dict[args.function]()
