<template>
  <div class="container">
  <div class="d-flex">

  </div>
  
  <table class="table">
  <thead>
    <tr>
      <th><abbr title="id">Product</abbr></th>
      <th>Image</th>
      <th><abbr title="Unit">Unit</abbr></th>
      <th><abbr title="Quantity">Qty</abbr></th>
      <th><abbr title="Price">Price</abbr></th>
      <th><abbr title="Total">Tot</abbr></th>
      <th><abbr title="Expiration day">ED</abbr></th>
      <th><abbr title="Category">Cat</abbr></th>
      <th><abbr title="Quantity left">QL</abbr></th>
      <th><abbr title="Options">Options</abbr></th>
    </tr>
  </thead>
  <tbody>
    <tr v-for="order in orders" :key="order.id">
      <th>{{ order.product.name }}</th>
      <td v-if="order.product.get_thumbnail"><img :src="order.product.get_thumbnail" alt=""></td>
      <td v-else>No image</td>
      <td>{{ order.product.unit }}</td>
      <td>{{ order.quantity }}</td>
      <td>{{ order.product.price }}</td>
      <td>{{ order.order_price }}</td>
      <td>{{ order.product.get_expiration_date }}</td>
      <td>{{ order.product.category.name }}</td>
      <td v-if="order.quantity_left < 1" class="text-danger">{{ order.quantity_left }}</td>
      <td v-else-if="order.quantity_left < 5" class="text-warning">{{ order.quantity_left }}</td>
      <td v-else>{{ order.quantity_left }}</td>
      <td>
        <div class="d-flex justify-content-evenly">

          <div title="Edit product">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pencil" viewBox="0 0 16 16">
            <path d="M12.146.146a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1 0 .708l-10 10a.5.5 0 0 1-.168.11l-5 2a.5.5 0 0 1-.65-.65l2-5a.5.5 0 0 1 .11-.168l10-10zM11.207 2.5 13.5 4.793 14.793 3.5 12.5 1.207 11.207 2.5zm1.586 3L10.5 3.207 4 9.707V10h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.5h.293l6.5-6.5zm-9.761 5.175-.106.106-1.528 3.821 3.821-1.528.106-.106A.5.5 0 0 1 5 12.5V12h-.5a.5.5 0 0 1-.5-.5V11h-.5a.5.5 0 0 1-.468-.325z"/>
            </svg>
          </div>
          <div title="Remove product" @click="removeProduct(order.id)">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-file-x" viewBox="0 0 16 16">
            <path d="M6.146 6.146a.5.5 0 0 1 .708 0L8 7.293l1.146-1.147a.5.5 0 1 1 .708.708L8.707 8l1.147 1.146a.5.5 0 0 1-.708.708L8 8.707 6.854 9.854a.5.5 0 0 1-.708-.708L7.293 8 6.146 6.854a.5.5 0 0 1 0-.708z"/>
            <path d="M4 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H4zm0 1h8a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1z"/>
            </svg>
          </div>
        </div>
                  
      </td>
    </tr>
  </tbody>
</table>
  
  </div>
</template>
<script>
import axios from 'axios';
export default {
  name: 'OrderList',
  props: {
    cartId: {
      type: Number,
      required: true
    }
  },
  data() {
    return {
      orders: [],
    }
  },
  methods: {
    async getOrders() {
      await axios.get(`orders/${this.cartId}/`)
        .then(response => {
          this.orders = response.data;
        })
        .catch(error => {
          console.log(error)
        })
    },
    // remove product from cart
    
    async removeProduct(id) {
      if (confirm('Are you sure you want to remove this product?')) {
        await axios.delete(`order/${id}/`)
          .then(response => {
            this.getOrders();
          })
          .catch(error => {
            console.log(error)
          })
      }
    }
  },

  mounted() {
    this.getOrders();
  },
}
</script>
<style scoped>
  img {
    max-width: 50px;
    max-height: 50px;
  }
  
</style>