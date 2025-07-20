import sqlite3
import numpy as np

# SQL script from the provided document
sql_script = """
CREATE TABLE retail_data (
  Store_ID TEXT,
  Footfall INTEGER,
  Promo_Spend INTEGER,
  Avg_Basket INTEGER,
  Returns INTEGER,
  Net_Sales INTEGER
);

INSERT INTO retail_data VALUES ('S04', 914, 2958, 85, 8, 78937);
INSERT INTO retail_data VALUES ('S09', 195, 646, 63, 6, 12419);
INSERT INTO retail_data VALUES ('S04', 272, 825, 70, 1, 19265);
INSERT INTO retail_data VALUES ('S05', 344, 1219, 84, 8, 29100);
INSERT INTO retail_data VALUES ('S10', 566, 1853, 41, 0, 24119);
INSERT INTO retail_data VALUES ('S10', 396, 2441, 67, 5, 27526);
INSERT INTO retail_data VALUES ('S08', 134, 1559, 33, 6, 4893);
INSERT INTO retail_data VALUES ('S08', 614, 2287, 29, 4, 18748);
INSERT INTO retail_data VALUES ('S01', 162, 797, 35, 5, 6042);
INSERT INTO retail_data VALUES ('S04', 999, 2519, 98, 9, 98561);
INSERT INTO retail_data VALUES ('S03', 993, 2693, 79, 0, 79687);
INSERT INTO retail_data VALUES ('S12', 886, 1644, 93, 6, 82940);
INSERT INTO retail_data VALUES ('S05', 318, 1516, 63, 9, 20258);
INSERT INTO retail_data VALUES ('S13', 591, 2576, 90, 1, 54266);
INSERT INTO retail_data VALUES ('S17', 377, 2970, 62, 6, 24621);
INSERT INTO retail_data VALUES ('S11', 423, 800, 36, 7, 15418);
INSERT INTO retail_data VALUES ('S08', 263, 2696, 85, 1, 23555);
INSERT INTO retail_data VALUES ('S03', 138, 2900, 54, 1, 8710);
INSERT INTO retail_data VALUES ('S10', 371, 1396, 78, 6, 29386);
INSERT INTO retail_data VALUES ('S15', 635, 2695, 82, 6, 53299);
INSERT INTO retail_data VALUES ('S11', 697, 790, 48, 5, 33468);
INSERT INTO retail_data VALUES ('S20', 356, 814, 28, 2, 10057);
INSERT INTO retail_data VALUES ('S11', 733, 2316, 63, 1, 47194);
INSERT INTO retail_data VALUES ('S07', 464, 2718, 54, 8, 25780);
INSERT INTO retail_data VALUES ('S07', 910, 1038, 98, 1, 89454);
INSERT INTO retail_data VALUES ('S13', 439, 2345, 95, 6, 42808);
INSERT INTO retail_data VALUES ('S06', 836, 2659, 27, 0, 24015);
INSERT INTO retail_data VALUES ('S14', 424, 2291, 38, 3, 17240);
INSERT INTO retail_data VALUES ('S09', 215, 2259, 41, 3, 9754);
INSERT INTO retail_data VALUES ('S05', 624, 2028, 55, 5, 35092);
INSERT INTO retail_data VALUES ('S08', 618, 1360, 36, 6, 22676);
INSERT INTO retail_data VALUES ('S16', 881, 2586, 32, 5, 29290);
INSERT INTO retail_data VALUES ('S07', 632, 1968, 82, 6, 52395);
INSERT INTO retail_data VALUES ('S14', 617, 1955, 22, 2, 14520);
INSERT INTO retail_data VALUES ('S05', 345, 723, 21, 1, 7494);
INSERT INTO retail_data VALUES ('S08', 308, 2483, 91, 3, 29295);
INSERT INTO retail_data VALUES ('S18', 234, 1966, 95, 7, 23101);
INSERT INTO retail_data VALUES ('S04', 409, 2969, 39, 7, 17266);
INSERT INTO retail_data VALUES ('S09', 697, 1946, 99, 10, 69368);
INSERT INTO retail_data VALUES ('S15', 467, 837, 99, 7, 46324);
INSERT INTO retail_data VALUES ('S20', 550, 2273, 28, 1, 16490);
INSERT INTO retail_data VALUES ('S04', 797, 2620, 96, 5, 77499);
INSERT INTO retail_data VALUES ('S14', 935, 2525, 29, 4, 28370);
INSERT INTO retail_data VALUES ('S20', 619, 2398, 84, 9, 52632);
INSERT INTO retail_data VALUES ('S02', 906, 1194, 73, 0, 66686);
INSERT INTO retail_data VALUES ('S19', 668, 2998, 40, 2, 28230);
INSERT INTO retail_data VALUES ('S19', 665, 2772, 39, 1, 27423);
INSERT INTO retail_data VALUES ('S01', 477, 2870, 36, 5, 18561);
INSERT INTO retail_data VALUES ('S19', 592, 2591, 76, 5, 46237);
INSERT INTO retail_data VALUES ('S06', 582, 872, 38, 8, 21928);
INSERT INTO retail_data VALUES ('S10', 886, 1492, 79, 4, 70618);
INSERT INTO retail_data VALUES ('S03', 745, 1754, 20, 5, 15756);
INSERT INTO retail_data VALUES ('S10', 179, 522, 82, 4, 14795);
INSERT INTO retail_data VALUES ('S13', 155, 1681, 33, 6, 5680);
INSERT INTO retail_data VALUES ('S17', 930, 990, 39, 10, 36056);
INSERT INTO retail_data VALUES ('S14', 847, 2982, 36, 7, 31824);
INSERT INTO retail_data VALUES ('S12', 829, 863, 51, 4, 42696);
INSERT INTO retail_data VALUES ('S13', 733, 2793, 87, 3, 64845);
INSERT INTO retail_data VALUES ('S06', 184, 1030, 75, 2, 14217);
INSERT INTO retail_data VALUES ('S19', 272, 1686, 83, 8, 22967);
INSERT INTO retail_data VALUES ('S18', 880, 2035, 78, 3, 69561);
INSERT INTO retail_data VALUES ('S16', 170, 2266, 55, 5, 10482);
INSERT INTO retail_data VALUES ('S15', 313, 1027, 85, 7, 26580);
INSERT INTO retail_data VALUES ('S15', 560, 2652, 79, 8, 45398);
INSERT INTO retail_data VALUES ('S19', 626, 1801, 90, 6, 57015);
INSERT INTO retail_data VALUES ('S15', 746, 729, 32, 10, 23662);
INSERT INTO retail_data VALUES ('S16', 346, 535, 90, 7, 31284);
INSERT INTO retail_data VALUES ('S11', 711, 1663, 87, 7, 62573);
INSERT INTO retail_data VALUES ('S14', 753, 2084, 61, 4, 46904);
INSERT INTO retail_data VALUES ('S11', 914, 1604, 86, 5, 79276);
INSERT INTO retail_data VALUES ('S18', 338, 2869, 55, 7, 19665);
INSERT INTO retail_data VALUES ('S15', 939, 2617, 87, 8, 82386);
INSERT INTO retail_data VALUES ('S06', 403, 1382, 84, 6, 34471);
INSERT INTO retail_data VALUES ('S19', 590, 1874, 47, 0, 28580);
INSERT INTO retail_data VALUES ('S10', 443, 2334, 68, 7, 30721);
INSERT INTO retail_data VALUES ('S18', 380, 2921, 46, 5, 18673);
INSERT INTO retail_data VALUES ('S20', 214, 704, 40, 4, 8826);
INSERT INTO retail_data VALUES ('S11', 161, 955, 69, 8, 11416);
INSERT INTO retail_data VALUES ('S04', 694, 2069, 37, 2, 26807);
INSERT INTO retail_data VALUES ('S11', 413, 2500, 76, 10, 32259);
INSERT INTO retail_data VALUES ('S02', 387, 1542, 59, 9, 23017);
INSERT INTO retail_data VALUES ('S19', 939, 2652, 99, 9, 93834);
INSERT INTO retail_data VALUES ('S20', 317, 1834, 42, 7, 13856);
INSERT INTO retail_data VALUES ('S09', 196, 2105, 45, 2, 9838);
INSERT INTO retail_data VALUES ('S01', 227, 2114, 38, 5, 9668);
INSERT INTO retail_data VALUES ('S20', 127, 1264, 52, 7, 6750);
INSERT INTO retail_data VALUES ('S16', 491, 2212, 85, 3, 42688);
INSERT INTO retail_data VALUES ('S09', 257, 1919, 33, 8, 8906);
INSERT INTO retail_data VALUES ('S02', 763, 2672, 38, 6, 30039);
INSERT INTO retail_data VALUES ('S06', 648, 2599, 39, 4, 26374);
INSERT INTO retail_data VALUES ('S15', 721, 2397, 79, 9, 57610);
INSERT INTO retail_data VALUES ('S08', 751, 1876, 67, 2, 51102);
INSERT INTO retail_data VALUES ('S03', 972, 560, 75, 6, 72653);
INSERT INTO retail_data VALUES ('S01', 391, 1845, 28, 7, 11756);
INSERT INTO retail_data VALUES ('S17', 638, 1032, 43, 6, 27828);
INSERT INTO retail_data VALUES ('S11', 369, 2582, 74, 4, 28624);
INSERT INTO retail_data VALUES ('S18', 652, 1468, 95, 5, 62598);
INSERT INTO retail_data VALUES ('S20', 687, 1992, 75, 5, 52428);
INSERT INTO retail_data VALUES ('S04', 434, 1175, 100, 4, 43554);
INSERT INTO retail_data VALUES ('S13', 214, 2156, 50, 3, 11613);
INSERT INTO retail_data VALUES ('S14', 135, 1130, 20, 10, 2867);
INSERT INTO retail_data VALUES ('S05', 855, 2161, 98, 8, 84483);
INSERT INTO retail_data VALUES ('S05', 806, 2968, 49, 4, 40796);
INSERT INTO retail_data VALUES ('S06', 945, 2103, 28, 9, 26882);
INSERT INTO retail_data VALUES ('S08', 408, 1440, 88, 0, 36674);
INSERT INTO retail_data VALUES ('S02', 745, 2850, 25, 7, 19670);
INSERT INTO retail_data VALUES ('S01', 193, 927, 74, 8, 14165);
INSERT INTO retail_data VALUES ('S12', 595, 2316, 45, 8, 27590);
INSERT INTO retail_data VALUES ('S02', 193, 1888, 38, 8, 7764);
INSERT INTO retail_data VALUES ('S05', 279, 2769, 87, 9, 25055);
INSERT INTO retail_data VALUES ('S18', 118, 620, 85, 4, 10311);
INSERT INTO retail_data VALUES ('S18', 746, 600, 36, 3, 26921);
INSERT INTO retail_data VALUES ('S17', 701, 890, 74, 10, 52054);
INSERT INTO retail_data VALUES ('S04', 515, 2098, 51, 4, 27141);
INSERT INTO retail_data VALUES ('S04', 249, 1687, 67, 2, 17549);
INSERT INTO retail_data VALUES ('S12', 132, 1775, 29, 4, 4724);
INSERT INTO retail_data VALUES ('S07', 240, 724, 50, 9, 11821);
INSERT INTO retail_data VALUES ('S12', 356, 1602, 79, 7, 28336);
INSERT INTO retail_data VALUES ('S11', 801, 2768, 89, 9, 72452);
INSERT INTO retail_data VALUES ('S18', 696, 1272, 90, 1, 63083);
INSERT INTO retail_data VALUES ('S03', 485, 780, 54, 4, 26572);
INSERT INTO retail_data VALUES ('S13', 486, 2857, 37, 1, 19581);
INSERT INTO retail_data VALUES ('S13', 161, 2736, 35, 10, 6556);
INSERT INTO retail_data VALUES ('S04', 574, 1636, 72, 1, 42094);
INSERT INTO retail_data VALUES ('S20', 920, 2132, 95, 2, 88571);
INSERT INTO retail_data VALUES ('S15', 886, 2185, 30, 1, 27435);
INSERT INTO retail_data VALUES ('S19', 267, 990, 67, 2, 18366);
INSERT INTO retail_data VALUES ('S10', 651, 2976, 84, 5, 56053);
INSERT INTO retail_data VALUES ('S14', 611, 1186, 81, 2, 49751);
INSERT INTO retail_data VALUES ('S17', 838, 2418, 70, 7, 59492);
INSERT INTO retail_data VALUES ('S17', 520, 2753, 40, 7, 21821);
INSERT INTO retail_data VALUES ('S05', 630, 855, 39, 3, 24940);
"""

# Connect to in-memory SQLite database
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Execute the SQL script
cursor.executescript(sql_script)
conn.commit()

# Extract data
cursor.execute("SELECT Returns, Avg_Basket, Net_Sales FROM retail_data")
data = cursor.fetchall()

# Convert to numpy array
data_array = np.array(data)

# Calculate correlation matrix (columns: Returns, Avg_Basket, Net_Sales)
corr_matrix = np.corrcoef(data_array, rowvar=False)

# Extract correlations
corr_returns_avg_basket = corr_matrix[0, 1]
corr_returns_net_sales = corr_matrix[0, 2]
corr_avg_basket_net_sales = corr_matrix[1, 2]

# Define pairs and their correlations
pairs = {
    "Returns-Avg_Basket": corr_returns_avg_basket,
    "Returns-Net_Sales": corr_returns_net_sales,
    "Avg_Basket-Net_Sales": corr_avg_basket_net_sales
}

# Find the pair with the strongest correlation (highest absolute value)
max_pair = max(pairs, key=lambda k: abs(pairs[k]))
max_correlation = round(pairs[max_pair], 2)

# Prepare JSON result
result = f'{{"pair": "{max_pair}", "correlation": {max_correlation}}}'

# Output the result (in practice, this would be written to a file and hosted)
print(result)

# Close the connection
conn.close()