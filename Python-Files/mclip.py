#! python3
# mclip.py - A multi-clipboard program.

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?""",
        'recruit': """Hey I saw your post on wowprogress and wanted to reach out and see if you'd be a good fit in my guild, Sanctuary - Bleeding Hollow (7/10M).
We raid Tues/Wed 9-12pm EST.

Here's our WowProgress page - https://www.wowprogress.com/guild/us/bleeding-hollow/Sanctuary
If you want to check out our raiding environment, here are some of our YouTube channels: https://www.youtube.com/channel/UCv3wEunfZssqp-Ct1g2PYxA/channels?view=49&shelf_id=3

Let me know if the hours work/you have any questions!"""}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: py mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1]    # first command line arg is the keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard.')
else:
    print('There is no text for ' + keyphrase)
