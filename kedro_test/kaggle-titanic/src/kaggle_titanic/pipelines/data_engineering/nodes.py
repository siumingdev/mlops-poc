import pandas as pd


def combine_kaggle_dataset(train_df: pd.DataFrame, test_df: pd.DataFrame) -> pd.DataFrame:
    train_df['is_test_set'] = False
    test_df['is_test_set'] = True
    return pd.concat([train_df, test_df])


def get_filled_age(df: pd.DataFrame) -> pd.Series:
    return df.groupby(['Sex', 'Pclass'])['Age'].apply(lambda x: x.fillna(x.median()))


def get_filled_embarked(df: pd.DataFrame) -> pd.Series:
    return df['Embarked'].fillna('S')


def get_filled_fare(df: pd.DataFrame) -> pd.Series:
    med_fare = df.groupby(['Pclass', 'Parch', 'SibSp']).Fare.median()[3][0][0]
    return df['Fare'].fillna(med_fare)


def get_deck_from_cabin(df: pd.DataFrame) -> pd.Series:
    df['Deck'] = df['Cabin'].apply(lambda s: s[0] if pd.notnull(s) else 'M')
    df.loc[df[df['Deck'] == 'T'].index, 'Deck'] = 'A'
    df['Deck'] = df['Deck'].replace(['A', 'B', 'C'], 'ABC')
    df['Deck'] = df['Deck'].replace(['D', 'E'], 'DE')
    df['Deck'] = df['Deck'].replace(['F', 'G'], 'FG')
    return df['Deck']


def get_family_size(df: pd.DataFrame) -> pd.Series:
    return df['SibSp'] + df['Parch'] + 1


def get_ticket_frequency(df: pd.DataFrame) -> pd.Series:
    return df.groupby('Ticket')['Ticket'].transform('count')


def get_title_from_name(df: pd.DataFrame) -> pd.Series:
    return df['Name'].str.split(', ', expand=True)[1].str.split('.', expand=True)[0]


def get_surname_from_name(df: pd.DataFrame) -> pd.Series:
    def extract_surname(name: str) -> str:
        import string

        if '(' in name:
            name_no_bracket = name.split('(')[0]
        else:
            name_no_bracket = name

        family = name_no_bracket.split(',')[0]
        # title = name_no_bracket.split(',')[1].strip().split(' ')[0]

        for c in string.punctuation:
            family = family.replace(c, '').strip()

        return family

    return df['Name'].map(extract_surname)


def get_master_table(
        raw_df: pd.DataFrame,
        age: pd.Series,
        embarked: pd.Series,
        fare: pd.Series,
        deck: pd.Series,
        family_size: pd.Series,
        ticket_frequency: pd.Series,
        title: pd.Series,
        surname: pd.Series) -> pd.DataFrame:
    df = raw_df
    df['Age'] = age
    df['Embarked'] = embarked
    df['Fare'] = fare
    df['Deck'] = deck
    df['Family_Size'] = family_size
    df['Ticket_Frequency'] = ticket_frequency
    df['Title'] = title
    df['Surname'] = surname
    return df
