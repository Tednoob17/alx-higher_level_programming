#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

int main()
{
&nbsp;&nbsp;seteuid( 1002 );
&nbsp;&nbsp;system( "/home/level2/random_dirs.sh" );
&nbsp;&nbsp;return 0;
}
