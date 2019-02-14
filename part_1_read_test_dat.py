import cc_dat_utils

#Part 1
input_dat_file = "C:/Users/Jonathan Namovic/Documents/Game design/Chips Challenge/cc_tools/data/pfgd_test.dat"

#Use cc_dat_utils.make_cc_data_from_dat() to load the file specified by input_dat_file
#print the resulting data

gameMap=cc_dat_utils.make_cc_data_from_dat(input_dat_file)

print(gameMap)