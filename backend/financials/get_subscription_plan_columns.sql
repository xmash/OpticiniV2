-- Get column information for financials_subscriptionplan table
-- Run this to see all columns and their data types

SELECT 
    column_name,
    data_type,
    character_maximum_length,
    is_nullable,
    column_default
FROM information_schema.columns
WHERE table_name = 'financials_subscriptionplan'
ORDER BY ordinal_position;

