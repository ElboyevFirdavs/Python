1.


      customers = pd.read_sql("SELECT * FROM Customer;", conn)
      invoices = pd.read_sql("SELECT * FROM Invoice;", conn)
      
      total_spent = invoices.groupby('CustomerId')['Total'].sum().reset_index()
    
      total_spent = total_spent.merge(customers[['CustomerId', 'FirstName', 'LastName']], on='CustomerId')
      total_spent['FullName'] = total_spent['FirstName'] + ' ' + total_spent['LastName']

      top_5 = total_spent.sort_values(by='Total', ascending=False).head(5)
      print("Top 5 Customers by Total Spent:")
      print(top_5[['CustomerId', 'FullName', 'Total']])

2.

      invoiceline = pd.read_sql("SELECT * FROM InvoiceLine;", conn)
      tracks = pd.read_sql("SELECT * FROM Track;", conn)
      albums = pd.read_sql("SELECT * FROM Album;", conn)
    
      invoice_track_album = invoiceline.merge(tracks[['TrackId', 'AlbumId']], on='TrackId')
      

      album_track_count = tracks.groupby('AlbumId')['TrackId'].nunique().reset_index()
      album_track_count.columns = ['AlbumId', 'TotalTracks']
      

      invoice_album_purchase = invoice_track_album.groupby(['InvoiceId', 'AlbumId'])['TrackId'].nunique().reset_index()
      invoice_album_purchase.columns = ['InvoiceId', 'AlbumId', 'PurchasedTracks']
      

      invoice_album_purchase = invoice_album_purchase.merge(album_track_count, on='AlbumId')
      invoice_album_purchase['FullAlbum'] = invoice_album_purchase['PurchasedTracks'] == invoice_album_purchase['TotalTracks']
      

      invoices = pd.read_sql("SELECT InvoiceId, CustomerId FROM Invoice;", conn)
      invoice_album_purchase = invoice_album_purchase.merge(invoices, on='InvoiceId')
      

      customer_pref = invoice_album_purchase.groupby('CustomerId')['FullAlbum'].any().reset_index()
      customer_pref.columns = ['CustomerId', 'BoughtFullAlbum']
      customer_pref['Preference'] = customer_pref['BoughtFullAlbum'].apply(lambda x: 'Full Album' if x else 'Individual Tracks')
      

      summary = customer_pref['Preference'].value_counts(normalize=True).reset_index()
      summary.columns = ['Preference', 'Percentage']
      summary['Percentage'] = (summary['Percentage'] * 100).round(2)
      
      print("\nCustomer Purchase Preferences:")
      print(summary)
