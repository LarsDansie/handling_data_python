open_file = open('CupcakeInvoices.csv')

# for row in open_file:
#     print(row)

# for row in open_file:
#     row = row.rstrip('\n').split(",")
#     for cupcakes in row:
#         if cupcakes == "Chocolate":
#             print("Chocolate")
#         elif cupcakes == "Vanilla":
#             print("Vanilla")
#         elif cupcakes == "Strawberry":
#             print("Strawberry")


# invoice_total = []

# for row in open_file:
#     row = row.rstrip('\n').split(",")
#     for receipt in row:
#         price = float(row[-1])
#         amount = float(row[-2])
#         total = amount * price
#     rounded_total = round(total, 2)
#     print(rounded_total)
#     invoice_total.append(rounded_total)

# print("=")
# final_amount = sum(invoice_total)

# rounded_final_amount = round(final_amount, 2)

# print(rounded_final_amount)




choc_amount = []
straw_amount = []
van_amount = []

for row in open_file:
    row = row.rstrip('\n').split(",")
    for cupcakes in row:
        price = float(row[-1])
        amount = float(row[-2])
        total = amount * price
        rounded_total = round(total, 2)
        if cupcakes == "Chocolate":
         choc_amount.append(rounded_total) 
        elif cupcakes == "Vanilla":
            van_amount.append(rounded_total)
        elif cupcakes == "Strawberry":
            straw_amount.append(rounded_total)



final_choc_amount = sum(choc_amount)
final_straw_amount = sum(straw_amount)
final_van_amount = sum(van_amount)

print("Chocolate total:", final_choc_amount)
print("Strawberry total:", final_straw_amount)
print("Vanilla total", final_van_amount)
