#!/usr/bin/perl -w
####################################################
#
# Perl source file for project gatecountopencv 
#
# <one line to give the program's name and a brief idea of what it does.>
#    Copyright (C) 2017  Andrew Nisbet, Edmonton Public Library
# The Edmonton Public Library respectfully acknowledges that we sit on
# Treaty 6 territory, traditional lands of First Nations and Metis people.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.
#
# Author:  Andrew Nisbet, Edmonton Public Library
# Created: Sat Oct 28 08:47:24 MDT 2017
# Rev: 
#          0.0 - Dev. 
#
####################################################

use strict;
use warnings;
use vars qw/ %opt /;
use Getopt::Std;

# Environment setup required by cron to run script because its daemon runs
# without assuming any environment settings and we need to use sirsi's.
###############################################
# *** Edit these to suit your environment *** #
$ENV{'PATH'}  = qq{:/s/sirsi/Unicorn/Bincustom:/s/sirsi/Unicorn/Bin:/usr/bin:/usr/sbin};
$ENV{'UPATH'} = qq{/s/sirsi/Unicorn/Config/upath};
###############################################
my $VERSION            = qq{0.0};
chomp( my $TEMP_DIR    = `getpathname tmp` );
chomp( my $TIME        = `date +%H%M%S` );
chomp ( my $DATE       = `date +%Y%m%d` );
my @CLEAN_UP_FILE_LIST = (); # List of file names that will be deleted at the end of the script if ! '-t'.
chomp( my $BINCUSTOM   = `getpathname bincustom` );
my $PIPE               = "$BINCUSTOM/pipe.pl";
chomp( my  = /home/ilsdev/projects/gatecountopencv );

#
# Message about this program and how to use it.
#
sub usage()
{
    print STDERR << "EOF";

	usage: $0 [-xt]
Usage notes for gatecountopencv.pl.
Transactions can be found in .

 -t: Preserve temporary files in $TEMP_DIR.
 -x: This (help) message.

example:
  $0 -x
Version: $VERSION
EOF
    exit;
}

# Logs an arbitrary set of strings to the log file. The log file is defined above and is never clobbered.
# params:  Strings or array of message strings. All params will be converted to strings for output.
# return:
sub logit
{
	my  =  . "/./create_EPLAPP_perl_project.sh.log";
	chomp( my  = 2017-10-28_08:47:24 );
	open( my , ">>",  ) or die( "** error opening log file '', \n" );
	foreach my  ( @_ )
	{
		print {  } sprintf "[%s] %s\n", , ;
	}
	close(  );
}

# Removes all the temp files created during running of the script.
# param:  List of all the file names to clean up.
# return: <none>
sub clean_up
{
	foreach my  ( @CLEAN_UP_FILE_LIST )
	{
		if ( {'t'} )
		{
			logit( sprintf( "preserving file '%s' for review.",  ) );
		}
		else
		{
			if ( -e  )
			{
				unlink ;
				logit( sprintf( "removed '%s'",  ) );
			}
		}
	}
}

# Writes data to a temp file and returns the name of the file with path.
# param:  unique name of temp file, like master_list, or 'hold_keys'.
# param:  data to write to file.
# return: name of the file that contains the list.
sub create_tmp_file( 31537 )
{
	my     = shift;
	my  = shift;
	my = sprintf "%02d", scalar @CLEAN_UP_FILE_LIST;
	my  = "/..Sat Oct 28 08:47:24 MDT 2017.";
	# Return just the file name if there are no results to report.
	return  if ( !  );
	# Adding append here so that 2 commands can output to the same file. Simplifies selections in deactivate.
	open FH, ">>" or die "*** error opening '', \n";
	print FH ;
	close FH;
	if ( grep( !/^()/, @CLEAN_UP_FILE_LIST ) )
	{
		# Add it to the list of files to clean if required at the end.
		push @CLEAN_UP_FILE_LIST, ;
	}
	logit( sprintf( "creating temp file '%s'",  ) );
	return ;
}

# Kicks off the setting of various switches.
# param:  
# return: 
sub init
{
    my $opt_string = 'tx';
    getopts( "$opt_string", \%opt ) or usage();
    usage() if ( $opt{'x'} );
}

init();

### code starts

### code ends
clean_up();
# EOF
