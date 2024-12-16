class EbayJsonExtractor:
    def __init__(self, item):
        if not isinstance(item, dict):
            raise ValueError("Expected item to be a dictionary.")
        self.item = item

    def extract_data(self):
        return {
            "item_information": (
                self.item.get('itemId'),
                self.item.get('title'),
                self.item.get('primaryCategory', {}).get('categoryId'),
                self.item.get('primaryCategory', {}).get('categoryName'),
                self.item.get('galleryURL'),
                self.item.get('viewItemURL'),
                self.item.get('productId', {}).get('value'),
                self.item.get('listingInfo', {}).get('listingType'),
                self.item.get('condition', {}).get('conditionId'),
                self.item.get('condition', {}).get('conditionDisplayName'),
                bool(self.item.get('isMultiVariationListing')),
                bool(self.item.get('topRatedListing'))
            ),
            "location_information": (
                self.item.get('itemId'),
                self.item.get('postalCode'),
                self.item.get('location'),
                self.item.get('country')
            ),
            "shipping_information": (
                self.item.get('itemId'),
                self.item.get('shippingInfo', {}).get('shippingServiceCost', {}).get('value'),
                self.item.get('shippingInfo', {}).get('shippingType'),
                bool(self.item.get('shippingInfo', {}).get('expeditedShipping')),
                bool(self.item.get('shippingInfo', {}).get('oneDayShippingAvailable')),
                self.item.get('shippingInfo', {}).get('handlingTime')
            ),
            "pricing_and_sales": (
                self.item.get('itemId'),
                self.item.get('sellingStatus', {}).get('currentPrice', {}).get('value'),
                self.item.get('sellingStatus', {}).get('convertedCurrentPrice', {}).get('value'),
                bool(self.item.get('listingInfo', {}).get('bestOfferEnabled')),
                bool(self.item.get('listingInfo', {}).get('buyItNowAvailable')),
                self.item.get('listingInfo', {}).get('startTime'),
                self.item.get('listingInfo', {}).get('endTime')
            ),
            "additional_attributes": (
                self.item.get('itemId'),
                self.item.get('globalId'),
                bool(self.item.get('autoPay', False)),
                self.item.get('sellingStatus', {}).get('timeLeft'),
                bool(self.item.get('listingInfo', {}).get('gift')),
                int(self.item.get('listingInfo', {}).get('watchCount', 0)),
                bool(self.item.get('returnsAccepted', False)),
                self.item.get('sellingStatus', {}).get('sellingState')
            )
        }
