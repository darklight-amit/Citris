CREATE TABLE citrisfinancial_report.NELNET_DAILY_FEED(
    LOANNUMBER      BIGINT,
EXTERNALREFID      VARCHAR(50),
LENDERNUMBER      INTEGER,
LENDERNAME      VARCHAR(50),
LENDERSHORTNAME      VARCHAR(50),
LENDERCREDITAGENCY      INTEGER,
LOANPROGRAMNUMBER      INTEGER,
LOAN_PROGRAM      VARCHAR(50),
BASERATECODE      VARCHAR(50),
INVESTORNUMBER      VARCHAR(50),
LOAN_AMOUNT      INTEGER,
INTEREST_RATE      NUMERIC,
LOAN_DUE_DAY      INTEGER,
LOAN_START_DATE      DATE,
MATURITY_DATE      DATE,
LOAN_MARGIN      NUMERIC,
LOAN_COMMUNICATION_SUPPRESSED      BOOLEAN,
COMMUNICATION_SUPPRESSION_BEGIN_DATE      VARCHAR(50),
NEXT_DUE_DATE      DATE,
NEXT_STMT_DATE      DATE,
TOTAL_AMOUNT_DUE      NUMERIC,
PAID_TO_DATE      DATE,
PARTIAL_PAYMENT_AMOUNT      NUMERIC,
LAST_PAYMENT_AMOUNT      NUMERIC,
LAST_PAYMENT_POST_DATE      DATE,
AUTO_DEBIT_PAYMENT_AMOUNT      NUMERIC,
LAST_AUTO_DEBIT_PMT_POST_DATE      DATE,
AUTO_DEBIT_INCENTIVE_ACTIVE      BOOLEAN,
TOTAL_INCENTIVE_RATE      NUMERIC,
AUTO_DEBIT_INCENTIVE_AMOUNT      NUMERIC,
IS_BANKRUPTCY_ACTIVE      BOOLEAN,
IS_DEATH_ACTIVE      BOOLEAN,
IS_DISABILITY_ACTIVE      BOOLEAN,
IS_SCRA_ACTIVE      BOOLEAN,
CURRENT_PRINCIPAL_BALANCE      NUMERIC,
INTEREST_ACCRUED      NUMERIC,
INTEREST_RECEIVED      NUMERIC,
INTEREST_ACCRUED_TO_DATE      DATE,
INTEREST_ACCRUED_THRU_DATE      DATE,
LOAN_STATUS      VARCHAR(50),
DAYS_LATE      INTEGER,
CURRENTAMOUNTDUE      NUMERIC,
PASTDUEAMOUNT      NUMERIC,
FEEAMOUNTDUE      NUMERIC,
LASTPAYMENTDATE      DATE,
LASTPAYMENTAMOUNT      NUMERIC,
FIRST_PAYMENT_DATE      DATE,
REGULAR_PAYMENT_AMOUNT      NUMERIC,
LOAN_TERM      INTEGER,
TERM_REMAINING      INTEGER,
TERM_FREQUENCY      VARCHAR(50),
DISBURSEMENT_1_ID      VARCHAR(50),
DISBURSEMENT_1_AMOUNT      NUMERIC,
DISBURSEMENT_1_DATE      DATE,
DISBURSEMENT_1_STATUS      VARCHAR(50),
DISBURSEMENT_1_ORIGINATION_FEE      NUMERIC,
DISBURSEMENT_1_ORIGINATION_FEE_TYPE      VARCHAR(50),
DISBURSEMENT_2_ID      VARCHAR(50),
DISBURSEMENT_2_AMOUNT      NUMERIC,
DISBURSEMENT_2_DATE      DATE,
DISBURSEMENT_2_STATUS      VARCHAR(50),
DISBURSEMENT_2_ORIGINATION_FEE      NUMERIC,
DISBURSEMENT_2_ORIGINATION_FEE_TYPE      VARCHAR(50),
DISBURSEMENT_3_ID      VARCHAR(50),
DISBURSEMENT_3_AMOUNT      NUMERIC,
DISBURSEMENT_3_DATE      DATE,
DISBURSEMENT_3_STATUS      VARCHAR(50),
DISBURSEMENT_3_ORIGINATION_FEE      NUMERIC,
DISBURSEMENT_3_ORIGINATION_FEE_TYPE      VARCHAR(50),
DISBURSEMENT_4_ID      VARCHAR(50),
DISBURSEMENT_4_AMOUNT      NUMERIC,
DISBURSEMENT_4_DATE      DATE,
DISBURSEMENT_4_STATUS      VARCHAR(50),
DISBURSEMENT_4_ORIGINATION_FEE      NUMERIC,
DISBURSEMENT_4_ORIGINATION_FEE_TYPE      VARCHAR(50),
DISBURSEMENT_5_ID      VARCHAR(50),
DISBURSEMENT_5_AMOUNT      NUMERIC,
DISBURSEMENT_5_DATE      DATE,
DISBURSEMENT_5_STATUS      VARCHAR(50),
DISBURSEMENT_5_ORIGINATION_FEE      NUMERIC,
DISBURSEMENT_5_ORIGINATION_FEE_TYPE      VARCHAR(50),
DISBURSEMENT_6_ID      VARCHAR(50),
DISBURSEMENT_6_AMOUNT      NUMERIC,
DISBURSEMENT_6_DATE      DATE,
DISBURSEMENT_6_STATUS      VARCHAR(50),
DISBURSEMENT_6_ORIGINATION_FEE      NUMERIC,
DISBURSEMENT_6_ORIGINATION_FEE_TYPE      VARCHAR(50),
DISBURSEMENT_7_ID      VARCHAR(50),
DISBURSEMENT_7_AMOUNT      NUMERIC,
DISBURSEMENT_7_DATE      DATE,
DISBURSEMENT_7_STATUS      VARCHAR(50),
DISBURSEMENT_7_ORIGINATION_FEE      NUMERIC,
DISBURSEMENT_7_ORIGINATION_FEE_TYPE      VARCHAR(50),
DISBURSEMENT_8_ID      VARCHAR(50),
DISBURSEMENT_8_AMOUNT      NUMERIC,
DISBURSEMENT_8_DATE      DATE,
DISBURSEMENT_8_STATUS      VARCHAR(50),
DISBURSEMENT_8_ORIGINATION_FEE      NUMERIC,
DISBURSEMENT_8_ORIGINATION_FEE_TYPE      VARCHAR(50),
DISBURSEMENT_9_ID      VARCHAR(50),
DISBURSEMENT_9_AMOUNT      NUMERIC,
DISBURSEMENT_9_DATE      DATE,
DISBURSEMENT_9_STATUS      VARCHAR(50),
DISBURSEMENT_9_ORIGINATION_FEE      NUMERIC,
DISBURSEMENT_9_ORIGINATION_FEE_TYPE      VARCHAR(50),
DISBURSEMENT_10_ID      VARCHAR(50),
DISBURSEMENT_10_AMOUNT      NUMERIC,
DISBURSEMENT_10_DATE      DATE,
DISBURSEMENT_10_STATUS      VARCHAR(50),
DISBURSEMENT_10_ORIGINATION_FEE      NUMERIC,
DISBURSEMENT_10_ORIGINATION_FEE_TYPE      VARCHAR(50),
DISBURSEMENT_11_ID      VARCHAR(50),
DISBURSEMENT_11_AMOUNT      NUMERIC,
DISBURSEMENT_11_DATE      DATE,
DISBURSEMENT_11_STATUS      VARCHAR(50),
DISBURSEMENT_11_ORIGINATION_FEE      NUMERIC,
DISBURSEMENT_11_ORIGINATION_FEE_TYPE      VARCHAR(50),
DISBURSEMENT_12_ID      VARCHAR(50),
DISBURSEMENT_12_AMOUNT      NUMERIC,
DISBURSEMENT_12_DATE      DATE,
DISBURSEMENT_12_STATUS      VARCHAR(50),
DISBURSEMENT_12_ORIGINATION_FEE      NUMERIC,
DISBURSEMENT_12_ORIGINATION_FEE_TYPE      VARCHAR(50),
DISBURSEMENT_13_ID      VARCHAR(50),
DISBURSEMENT_13_AMOUNT      NUMERIC,
DISBURSEMENT_13_DATE      DATE,
DISBURSEMENT_13_STATUS      VARCHAR(50),
DISBURSEMENT_13_ORIGINATION_FEE      NUMERIC,
DISBURSEMENT_13_ORIGINATION_FEE_TYPE      VARCHAR(50),
DISBURSEMENT_14_ID      VARCHAR(50),
DISBURSEMENT_14_AMOUNT      NUMERIC,
DISBURSEMENT_14_DATE      DATE,
DISBURSEMENT_14_STATUS      VARCHAR(50),
DISBURSEMENT_14_ORIGINATION_FEE      NUMERIC,
DISBURSEMENT_14_ORIGINATION_FEE_TYPE      VARCHAR(50),
DISBURSEMENT_15_ID      VARCHAR(50),
DISBURSEMENT_15_AMOUNT      NUMERIC,
DISBURSEMENT_15_DATE      DATE,
DISBURSEMENT_15_STATUS      VARCHAR(50),
DISBURSEMENT_15_ORIGINATION_FEE      NUMERIC,
DISBURSEMENT_15_ORIGINATION_FEE_TYPE      VARCHAR(50),
AUTODEBIT_AUTODEBITID      VARCHAR(50),
AUTODEBIT_ISACTIVE      BOOLEAN,
AUTODEBIT_ACCOUNTTYPE      VARCHAR(50),
AUTODEBIT_ROUTINGNUMBER      INTEGER,
BR_BORROWER_NUMBER      BIGINT,
BR_FIRST_NAME      VARCHAR(50),
BR_LAST_NAME      VARCHAR(50),
BR_MIDDLE_NAME      VARCHAR(50),
BR_SUFFIX      VARCHAR(50),
BR_DOB      DATE,
BR_SSN      BIGINT,
BR_HOME_CITY      VARCHAR(50),
BR_HOME_STATE      VARCHAR(50),
BR_HOME_POSTALCODE      VARCHAR(50),
BR_HOME_COUNTRYCODE      VARCHAR(50),
BR_HOME_STREET1      VARCHAR(50),
BR_HOME_STREET2      VARCHAR(50),
BR_HOME_ISVALID      BOOLEAN,
BR_ADDRESS_EFF_DATE      DATE,
BR_HOME_PHONE      BIGINT,
BR_PHONE_EFF_DATE      DATE,
BR_PHONE_ISVALID      BOOLEAN,
BR_HOME_PHONE_HAS_CONSENT      BOOLEAN,
BR_HOME_PHONE_CONSENT_EFF_DATE_TIME      VARCHAR(50),
BR_EMAIL_ADDRESS      VARCHAR(50),
BR_EMAIL_EFF_DATE      DATE,
BR_EMAIL_ISVALID      BOOLEAN,
BR_ECORRACCEPTED      VARCHAR(50),
BR_SCORE      VARCHAR(50),
CS_BORROWER_NUMBER      VARCHAR(50),
CS_FIRST_NAME      VARCHAR(50),
CS_LAST_NAME      VARCHAR(50),
CS_MIDDLE_NAME      VARCHAR(50),
CS_SUFFIX      VARCHAR(50),
CS_DOB      VARCHAR(50),
CS_SSN      VARCHAR(50),
CS_HOME_CITY      VARCHAR(50),
CS_HOME_STATE      VARCHAR(50),
CS_HOME_POSTALCODE      VARCHAR(50),
CS_HOME_COUNTRYCODE      VARCHAR(50),
CS_HOME_STREET1      VARCHAR(50),
CS_HOME_STREET2      VARCHAR(50),
CS_HOME_ISVALID      VARCHAR(50),
CS_HOME_PHONE_HAS_CONSENT      VARCHAR(50),
CS_HOME_PHONE_CONSENT_EFF_DATE_TIME      VARCHAR(50),
CS_ADDRESS_EFF_DATE      VARCHAR(50),
CS_HOME_PHONE      VARCHAR(50),
CS_PHONE_EFF_DATE      VARCHAR(50),
CS_PHONE_ISVALID      VARCHAR(50),
CS_EMAIL_ADDRESS      VARCHAR(50),
CS_EMAIL_EFF_DATE      VARCHAR(50),
CS_EMAIL_ISVALID      VARCHAR(50),
CS_ECORRACCEPTED      VARCHAR(50),
CS_SCORE      VARCHAR(50),
ONBOARDING_ID      VARCHAR(50),
SCHOOL_NAME      VARCHAR(50),
SCHOOL_CODE      VARCHAR(50),
SCHOOL_ATTENDANCE_DATE      VARCHAR(50),
ENROLLMENT_CERTIFICATION_DATE      VARCHAR(50),
ENROLLMENT_STATUS_BEGIN_DATE      VARCHAR(50),
ENROLLMENT_RECEIVED_DATE      VARCHAR(50),
ENROLLMENT_GRADUATION_DATE      VARCHAR(50),
ENROLLMENT_TERM_BEGIN_DATE      VARCHAR(50),
ENROLLMENT_TERM_END_DATE      VARCHAR(50),
ENROLLMENT_STATUS      VARCHAR(50),
ENROLLMENT_STATUS_CODE      VARCHAR(50),
ENROLLMENT_SOURCE      VARCHAR(50)
);