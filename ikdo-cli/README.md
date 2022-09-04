# ikdo app

## final design idea

Main "list" ui:

```
<list name>                                         @<author>
________________________________________________________________________
[ ] <item 1 name>                      1| <selected item content>
[ ] <item 2 name>         (<deadline>) 2| <in markdown>
[*] <item 3 name>                      1|
[*] <item 4 name>                      1|
[ ] <item 5 name>                      1|
### _____________________ ____________ _|
```

Lists Dashboards:
```
_______________________________________________________  most recent  __
<list 1 name>                  @<author>| [ ] <list name>: <item name>
<list 2 name>                  @<author>| [ ] <list name>: <item name> 
### ____________________________________| [ ] <list name>: <item name>
                                        | [ ] <list name>: <item name>
                                        | [ ] <list name>: <item name>
                                        | [ ] <list name>: <item name>
```


## interractions

#### main list ui:

[ ] up down: j/k and arrow keys
[ ] toggle todo: space
[ ] insert mode: enter (on both existing items and new ones)
[ ] go to content pane : left arrow and l
[ ] back from content pane : esc (allow using tab key in content)
[ ] update priority: +/- and ^x/^a
[ ] go to dashboard: h and left arrow

#### dashboard

[ ] go to list



#### "cloud" mode:

[ ] share: "i" to generate invite link (for selected list in dashboard or current list in list view)
