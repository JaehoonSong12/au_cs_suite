#!/usr/bin/perl
use strict;
use warnings;

# Input and output file paths
my $input_file  = 'raw_data.tsv';
my $output_file = 'aggregated_data.tsv';

# Open the input file for reading
open my $in_fh, '<', $input_file or die "Cannot open $input_file: $!";

# Read the header line
my $header = <$in_fh>;
chomp $header;
my @columns = split /\t/, $header;

# Create a hash to store aggregated data
my %aggregated;

# Process each line in the input file
while (my $line = <$in_fh>) {
    chomp $line;
    my @fields = split /\t/, $line;
    my $id = $fields[0];
    my $salary = $fields[4];

    # Initialize the aggregation for the ID if not already done
    if (!exists $aggregated{$id}) {
        $aggregated{$id} = {
            name       => $fields[1],
            age        => $fields[2],
            country    => $fields[3],
            total_salary => 0,
            hire_date  => $fields[8],
            status     => $fields[10],
        };
    }

    # Add the salary to the total
    $aggregated{$id}->{total_salary} += $salary;
}
close $in_fh;

# Open the output file for writing
open my $out_fh, '>', $output_file or die "Cannot open $output_file: $!";

# Write the header to the output file
print $out_fh "id\tname\tage\tcountry\ttotal_salary\thire_date\tstatus\n";

# Write the aggregated data to the output file
for my $id (sort { $a <=> $b } keys %aggregated) {
    my $data = $aggregated{$id};
    print $out_fh join("\t",
        $id,
        $data->{name},
        $data->{age},
        $data->{country},
        $data->{total_salary},
        $data->{hire_date},
        $data->{status}
    ), "\n";
}
close $out_fh;

print "Aggregated data written to $output_file\n";
