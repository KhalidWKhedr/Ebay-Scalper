import csv

class EbayData:
    def __init__(self, json_data):
        self.item_json = json_data[0]
        self.items = self.item_json.get('searchResult', {}).get('item', [])
        self.csv_file = json_data[1] + '.output_csv'
        self.save_path = 'output_csv'

    def write_to_csv(self):
        csv_columns = [
            'itemId', 'title', 'globalId', 'categoryId', 'categoryName', 'galleryURL', 'viewItemURL',
            'productId', 'autoPay', 'postalCode', 'location', 'country', 'shippingCost', 'shippingType',
            'expeditedShipping', 'oneDayShippingAvailable', 'handlingTime', 'currentPrice', 'convertedCurrentPrice',
            'sellingState', 'timeLeft', 'bestOfferEnabled', 'buyItNowAvailable', 'startTime', 'endTime',
            'listingType', 'gift', 'watchCount', 'returnsAccepted', 'conditionId', 'conditionDisplayName',
            'isMultiVariationListing', 'topRatedListing'
        ]

        # Open CSV file and write data
        with open(self.csv_file, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()  # Write column headers

            for item in self.items:
                # Flatten the data structure to fit CSV format
                csv_row = {
                    'itemId': item.get('itemId'),
                    'title': item.get('title'),
                    'globalId': item.get('globalId'),
                    'categoryId': item.get('primaryCategory', {}).get('categoryId'),
                    'categoryName': item.get('primaryCategory', {}).get('categoryName'),
                    'galleryURL': item.get('galleryURL'),
                    'viewItemURL': item.get('viewItemURL'),
                    'productId': item.get('productId', {}).get('value') if item.get('productId') else None,
                    'autoPay': item.get('autoPay'),
                    'postalCode': item.get('postalCode'),
                    'location': item.get('location'),
                    'country': item.get('country'),
                    'shippingCost': item.get('shippingInfo', {}).get('shippingServiceCost', {}).get('value') if item.get('shippingInfo') else None,
                    'shippingType': item.get('shippingInfo', {}).get('shippingType'),
                    'expeditedShipping': item.get('shippingInfo', {}).get('expeditedShipping'),
                    'oneDayShippingAvailable': item.get('shippingInfo', {}).get('oneDayShippingAvailable'),
                    'handlingTime': item.get('shippingInfo', {}).get('handlingTime'),
                    'currentPrice': item.get('sellingStatus', {}).get('currentPrice', {}).get('value') if item.get('sellingStatus') else None,
                    'convertedCurrentPrice': item.get('sellingStatus', {}).get('convertedCurrentPrice', {}).get('value') if item.get('sellingStatus') else None,
                    'sellingState': item.get('sellingStatus', {}).get('sellingState'),
                    'timeLeft': item.get('sellingStatus', {}).get('timeLeft'),
                    'bestOfferEnabled': item.get('listingInfo', {}).get('bestOfferEnabled'),
                    'buyItNowAvailable': item.get('listingInfo', {}).get('buyItNowAvailable'),
                    'startTime': item.get('listingInfo', {}).get('startTime'),
                    'endTime': item.get('listingInfo', {}).get('endTime'),
                    'listingType': item.get('listingInfo', {}).get('listingType'),
                    'gift': item.get('listingInfo', {}).get('gift'),
                    'watchCount': item.get('listingInfo', {}).get('watchCount'),
                    'returnsAccepted': item.get('returnsAccepted'),
                    'conditionId': item.get('condition', {}).get('conditionId'),
                    'conditionDisplayName': item.get('condition', {}).get('conditionDisplayName'),
                    'isMultiVariationListing': item.get('isMultiVariationListing'),
                    'topRatedListing': item.get('topRatedListing')
                }

                # Write row to CSV
                writer.writerow(csv_row)

        print(f"Data successfully written to {self.csv_file}")
