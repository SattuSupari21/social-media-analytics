if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(df, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here

    # Derived Metrics
    df['Engagement_Rate'] = ((df['Likes'] + df['Comments']) / df['Views']) * 100
    df['Virality_Score'] = (df['Shares'] / df['Views']) * 100
    df['Like_to_Share_Ratio'] = (df['Likes'] / df['Shares']) * 100
    df['Comments_to_Likes'] = (df['Comments'] / df['Likes']) * 100

    # Feature Engineering
    dim_hashtag = df[['Hashtag']].drop_duplicates().reset_index(drop=True)
    dim_hashtag['Hashtag_ID'] = dim_hashtag.index
    dim_hashtag = dim_hashtag[['Hashtag_ID', 'Hashtag']]

    dim_region = df[['Region']].drop_duplicates().reset_index(drop=True)
    dim_region['Region_ID'] = dim_region.index
    dim_region = dim_region[['Region_ID', 'Region']]

    dim_platform = df[['Platform']].drop_duplicates().reset_index(drop=True)
    dim_platform['Platform_ID'] = dim_platform.index
    dim_platform = dim_platform[['Platform_ID', 'Platform']]

    dim_content_type = df[['Content_Type']].drop_duplicates().reset_index(drop=True)
    dim_content_type['Content_Type_ID'] = dim_content_type.index
    dim_content_type = dim_content_type[['Content_Type_ID', 'Content_Type']]

    # Merge all tables in a new dataframe
    new_df = df.merge(dim_hashtag, on='Hashtag')\
            .merge(dim_region, on='Region')\
            .merge(dim_platform, on='Platform')\
            .merge(dim_content_type, on='Content_Type')\
            [['Post_ID', 'Hashtag_ID', 'Region_ID', 'Platform_ID', 'Content_Type_ID',\
              'Platform', 'Hashtag', 'Content_Type', 'Region', 'Views',\
              'Likes', 'Shares', 'Comments', 'Engagement_Level', 'Engagement_Rate',\
              'Virality_Score', 'Like_to_Share_Ratio', 'Comments_to_Likes']]


    return new_df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
