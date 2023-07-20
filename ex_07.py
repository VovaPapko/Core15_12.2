text = [{"line1": "Dignissim eleifend dolores sed nonummy voluptua invidunt augue.",
"line2": "Invidunt eum aliquyam accusam feugiat erat esse diam et zzril ipsum."},
{"line3": "Ea consetetur sit lorem amet et ut stet eirmod esse aliquyam nulla.",
"line4": "Elitr volutpat sea voluptua facilisis nulla kasd elit eos magna."}]


search = "no"

result = []

for i in text:
    if search in str(i):
        result.append(i)

print(result)