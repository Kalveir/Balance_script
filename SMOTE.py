import pandas as pd
from imblearn.over_sampling import SMOTE

# Membaca data dari file CSV
df = pd.read_csv('data.csv')

# Memisahkan fitur dan label
X = df.drop('label', axis=1)
y = df['label']

# Inisialisasi objek SMOTE
smote = SMOTE()

# Melakukan oversampling menggunakan SMOTE
X_resampled, y_resampled = smote.fit_resample(X, y)

# Menyusun data hasil oversampling menjadi dataframe baru
df_resampled = pd.concat([pd.DataFrame(X_resampled, columns=X.columns), pd.Series(y_resampled, name='label')], axis=1)

# Menyimpan data hasil oversampling ke file CSV
df_resampled.to_csv('data_oversampled.csv', index=False)
