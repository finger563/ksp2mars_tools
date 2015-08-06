/*
 * KSP Craft file grammar
 * Author: William Emfinger
 * Date: 2015.08.05
 */

grammar ksp_craft;

/*
 * This is the start of our craft file
 */
start
    :   ('ship' '=' ship)
        ('version' '=' version)
        ('description' '=' description)
        ('type' '=' kind)
        ('size' '=' size)
        (part)*
        EOF
    ;

ship
    :   ID
    ;

partname
    :   ID
    ;

version
    :   ID
    ;

description
    :   ID
    ;

kind
    :   ID
    ;

size
    :   ID
    ;

uuid
    :   ID
    ;

link_uuid
    :   ID
    ;

attn_uuid
    :   ID
    ;

/*
 * Define a part Type
 */
part
    :   'PART'
        '{'
        ( 'part' '=' uuid )
        ( 'partName' '=' partname )
        ( 'pos' '=' partname )
        ( 'attPos' '=' partname )
        ( 'attPos0' '=' partname )
        ( 'rot' '=' partname )
        ( 'attRot' '=' partname )
        ( 'attRot0' '=' partname )
        ( 'mir' '=' partname )
        ( 'symMethod' '=' partname )
        ( 'link' '=' link_uuid )*
        ( 'attN' '=' attn_uuid )*
        ( events )
        ( actions )
        ( partdata )
        ( module )*
        '}'
    ;

events
    :   'EVENTS'
        '{'
        '}'
    ;
actions
    :   'ACTIONS'
        '{'
        '}'
    ;
partdata
    :   'PARTDATA'
        '{'
        '}'
    ;
module
    :   'MODULE'
        '{'
        '}'
    ;

// An ID - one or more alphanumeric characters that must start with either an alphabet/underscore
ID
    :   ( 'a'..'z' | 'A'..'Z' | '0'..'9' | ',' | '_' | '-' | ':' | '.' | '/' | '(' | ')' )
        ( 'a'..'z' | 'A'..'Z' | '0'..'9' | ',' | '_' | '-' | ':' | '.' | '/' | '(' | ')' )*
    ;


// White spaces and escape codes are ignored
WS
    :   ( (' ')*
        | '\t'
        | '\r'
        | '\n'
        ) -> channel(HIDDEN)
    ;
