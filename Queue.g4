grammar Queue;

prog: stmts EOF;

stmts: stmt+;

stmt:  create = createQueue '.' NEWLINE
| basicQueueOptions = queueOptions '.' NEWLINE
| printOptions = printQueueOptions '.' NEWLINE
| booleanQueueOptions = booleanQueue '?' NEWLINE
| miscQueueOptions = miscQueue '.' NEWLINE
| exitQueue = exQueue '.' NEWLINE
;

createQueue:
'Create' '[' queueName = ID ']' '[' queueSize = INT ']'
|'Spawn' '[' queueName = ID ']' '[' queueSize = INT ']'
;

queueOptions:
enqueue = enqueueOptions
|remove = dequeue
|erase = clear
;

enqueueOptions:
'Enqueue' '[' queueName = ID ']' '[' elements = NAME ']' '[' priority = INT']'
| 'Enqueue' '[' queueName = ID ']' '[' elements = TWITTERHANDLE ']' '[' priority = INT']'
| 'Enqueue' '[' queueName = ID ']' '[' elements = IP ']' '[' priority = INT']'
| 'Enqueue' '[' queueName = ID ']' '[' elements = DISCORD ']' '[' priority = INT']'
| 'EQ' '[' queueName = ID ']' '[' elements = NAME ']' '[' priority = INT']'
| 'EQ' '[' queueName = ID ']' '[' elements = TWITTERHANDLE ']' '[' priority = INT']'
| 'EQ' '[' queueName = ID ']' '[' elements = IP ']' '[' priority = INT']'
| 'EQ' '[' queueName = ID ']' '[' elements = DISCORD ']' '[' priority = INT']'
;

dequeue: 'Dequeue' '[' queueName = ID ']'
|'DQ' '[' queueName = ID ']'
;

clear: 'Clear' '[' queueName = ID ']'
|'C' '[' queueName = ID ']'
|'Respawn' '[' queueName = ID ']'
;

printQueueOptions:
'Print' queue = theQueue
|'Print' element=elemental
|'Print' head=heads
|'Print' tail=tails
|'Output' queue = theQueue
|'Output' element=elemental
|'Output' head=heads
|'Output' tail=tails
;

theQueue: 'queue' '[' queueName = ID ']';
elemental: 'element' 'from' '[' queueName = ID ']' 'with' 'priority' '[' priority = INT ']';
heads: 'head' '[' queueName = ID ']';
tails: 'tail' '[' queueName = ID ']';

booleanQueue:
'Is' emp=empty
| 'Is' pop=populated
| 'Is' in=inside
;

empty: '[' queueName = ID ']' 'empty';
populated: '[' queueName = ID ']' 'populated';
inside: '[' elementName = NAME ']' 'inside' '[' queueName = ID ']'
|'[' elementName = TWITTERHANDLE ']' 'inside' '[' queueName = ID ']'
|'[' elementName = IP ']' 'inside' '[' queueName = ID ']'
|'[' elementName = DISCORD ']' 'inside' '[' queueName = ID ']';

miscQueue:
swappa = swap
| combinatory = combine
| noU = reverse
;

swap: 'Swap' 'queue' '[' queueName = ID ']' 'with' '[' queueNameTwo = ID ']'
| '[' queueName = ID ']' '<->' '[' queueNameTwo = ID ']'
| 'Soul' 'swap' '[' queueName = ID ']' '[' queueNameTwo = ID ']'
;
combine: 'Combine' 'queues' '[' queueName = ID ']' '[' queueNameTwo = ID ']'
| 'Concatenate' 'queues' '[' queueName = ID ']' '[' queueNameTwo = ID ']'
| '[' queueName = ID']' '+' '[' queueNameTwo = ID ']'
;
reverse: 'Reverse' 'queue' '[' queueName = ID ']'
|'[' queueName = ID ']' 'R'
| 'Reverse' 'card' 'on' 'queue' '[' queueName = ID ']'
;

exQueue:
'Exit' 'from' '[' queueName = ID ']' '[' elementName = NAME ']'
| 'Exit' 'from' '[' queueName = ID ']' '[' elementName = TWITTERHANDLE ']'
| 'Exit' 'from' '[' queueName = ID ']' '[' elementName = IP ']'
| 'Exit' 'from' '[' queueName = ID ']' '[' elementName = DISCORD ']'
|'X' 'out' '[' elementName = NAME ']' 'from' '[' queueName = ID ']'
|'X' 'out' '[' elementName = TWITTERHANDLE ']' 'from' '[' queueName = ID ']'
|'X' 'out' '[' elementName = IP ']' 'from' '[' queueName = ID ']'
|'X' 'out' '[' elementName = DISCORD ']' 'from' '[' queueName = ID ']'

;

NEWLINE : [\r\n]+ ;
INT: [0-9]+ ;
ID: [a-zA-Z0-9]+;
NAME: [A-Z][a-z]+' '[A-Z][a-z]+ ' ' '*' [0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9];
TWITTERHANDLE:'@'[A-Za-z0-9]+;
IP:[0-9][0-9]'.'[0-9][0-9][0-9]'.'[0-9][0-9][0-9]'.'[0-9][0-9];
DISCORD: [a-zA-Z_0-9 ]+'#'[0-9][0-9][0-9][0-9];
WS: [ \t\n\r\f]+ -> channel(HIDDEN) ;