def getFunction( ) :
    functionInput = input( "Enter the function: " ) 
    return lambda x: eval( functionInput )


def bisection( function, a, b ) :
    if ( function( a ) * function( b )  >= 0 ) :
        print("Conditions for bisection method not met. ")
        return 
    
    c = a 
    while ( b - a >= 0.01 ) :
        
        c = ( a + b ) / 2  

        if ( function( c ) == 0 ) :
            break

        if ( function( a ) * function( c )  < 0 ) :
            b = c 

        else :
            a = c 

        
    print("The value of root is : ","%.4f"%c)

functionCheck = getFunction()
value1 = ( int ( input ( "Enter the first limit: " ) ) )
value2 = ( int ( input ( "Enter the second limit: " ) ) )

bisection( functionCheck, value1 , value2 )
