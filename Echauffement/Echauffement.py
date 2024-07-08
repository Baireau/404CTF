secret_data_hex_list = [
    "68", "5F", "66", "83", "A4", "87", "F0", "D1", "B6", "C1", "BC", "C5", "5C", "DD", "BE", "BD",
    "56", "C9", "54", "C9", "D4", "A9", "50", "CF", "D0", "A5", "CE", "4B", "C8", "BD", "44", "BD",
    "AA", "D9"
]

result_list = []

for i, hex_value in enumerate(secret_data_hex_list):
    decimal_value = int(hex_value, 16)
    modified_value = (decimal_value + i) / 2
    result_list.append(modified_value)

print("Liste résultante en Décimale :", result_list)
ascii_values = [chr(int(value)) for value in result_list]
print("Liste résultante en ASCII :", ''.join(ascii_values))
