import pandas as pd

dataset = 'A-n32-k5'
# dataset = 'CMT1'
# dataset = 'CMT2'

coord_path = f'files/{dataset}_coord.xlsx'
demanda_path = f'files/{dataset}_demanda.xlsx'

with open(f'files/{dataset}_cap.txt', 'r') as file:
    cap = int(file.read())

df_coord = pd.read_excel(coord_path)
df_demanda = pd.read_excel(demanda_path)

# se crea el df que se refiere a las coordenadas junto a su respectiva demanda y el cálculo de su tangente
tans = []
dems = []
for i in range(len(df_coord)):
    tan = df_coord.iloc[i]['y'] / df_coord.iloc[i]['x']
    demanda = df_demanda.iloc[i]['demanda']
    dems.append(demanda)
    tans.append(tan)

df_coord['demanda'] = dems
df_coord['tan'] = tans

# se ordena el df de las coordenadas con su tangente de mayor a menor
df_coord = df_coord.sort_values(by='tan', ascending=False)
print(df_coord)

# se declaran los valores que nos permitiran tener la información de las rutas finales
current_cap = 0
current_route = []
results_df = pd.DataFrame(columns=['Ruta', 'Demanda Acumulada', 'Capacidad Restante'])

# se itera por cada nodo para comprobar si cabe en la ruta actual o no
for i in range(len(df_coord)):
    current_node = int(df_coord.iloc[i]['n'])

    # en caso de caber, se agrega a la ruta actual
    if(current_cap + df_coord.iloc[i]['demanda'] <= cap):
        current_cap += df_coord.iloc[i]['demanda']
        current_route.append(current_node)

    # en caso de no caber, se crea una ruta nueva y se inserta la ruta actual en la lista de rutas finales
    else:
        current_route_string = "-".join(map(str, current_route))
        new_data = new_data = {'Ruta': current_route_string, 'Demanda Acumulada': int(current_cap), 'Capacidad Restante': cap - int(current_cap)}
        results_df = pd.concat([results_df, pd.DataFrame(new_data, index=[0])], ignore_index=True)

        current_cap = 0
        current_route.clear()

        current_cap += df_coord.iloc[i]['demanda']
        current_route.append(current_node)

    # en caso de ser el último nodo, se agrega toda la ruta que no había podido ser guardada en la lista final
    if(i == len(df_coord) - 1):
        current_route_string = "-".join(map(str, current_route))
        new_data = new_data = {'Ruta': current_route_string, 'Demanda Acumulada': int(current_cap), 'Capacidad Restante': cap - int(current_cap)}
        results_df = pd.concat([results_df, pd.DataFrame(new_data, index=[0])], ignore_index=True)

# se muestra el df de las rutas finales
print(results_df)

