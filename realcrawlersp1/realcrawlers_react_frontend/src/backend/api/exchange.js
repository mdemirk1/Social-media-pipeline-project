
export const getCryptoExchange = async (crypto) => {
    const response = await fetch(`/api/get_cyptocurrency/${crypto}`);
    const data = await response.json();
    //console.log(data);
    const dataArray = [];

    const keys = Object.keys(data["Time Series (Digital Currency Daily)"]);
    const startIndex = Math.max(keys.length - 100, 0);
    const last100Keys = keys.slice(startIndex);

    // Iterate through the keys of the outer object
    for (const date of last100Keys) {
        if (data["Time Series (Digital Currency Daily)"].hasOwnProperty(date)) {
            // Extract data for the current date
            const dateData = data["Time Series (Digital Currency Daily)"][date];
            const dateObject = {
            date: date,
            ...dateData
            };

            dataArray.push(dateObject);
        }
    }
    console.log(dataArray)
    return dataArray
  };