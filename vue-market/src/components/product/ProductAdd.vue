<template>
  <div class="container">
    <h3 class="text-center title">Add Product to {{ this.$route.params.name }}</h3>
    <form class="container" @submit.prevent enctype="multipart/form-data">
      <div class="mb-3">
        <label for="inputTitle" class="form-label">Title</label>
        <input type="text" class="form-control" id="inputTitle" v-model="product.name" required>
        <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
      </div>
      <div class="mb-3">
        <label for="inputDescription" class="form-label" >Description</label>
        <input type="textarea" class="form-control" id="inputDescription" v-model="product.description" required>
      </div>
      <div class="mb-3">
        <label for="inputPrice" class="form-label" >Price</label>
        <input type="number" class="form-control" id="inputPrice" v-model="product.price" required>
      </div>
      <div class="mb-3">
        <label for="inputUnit" class="form-label" >Unit</label>
        <select class="form-select" aria-label="Default select example" v-model="product.unit">
          <option v-for="unit in units" :value="unit">{{ unit }}</option>
        </select>
      </div>
      <div class="mb-3">
        <label for="inputQuantity" class="form-label" >Quantity</label>
        <input type="number" class="form-control" id="inputQuantity" v-model="product.quantity" required>
      </div>
      <div class="mb-3">
        <label for="inputBarcode" class="form-label" >Barcode</label>
        <input type="number" class="form-control" id="inputBarcode" v-model="product.barcode" required>
      </div>
      <div class="mb-3 form-check">
        <label for="inputIsExpired" class="form-label" >Is expired</label>
        <input type="checkbox" class="form-check-input" id="inputIsExpired" v-model="product.is_expired">
      </div>
      <div class="mb-3" v-if="product.is_expired">
        <label for="inputExpirationDate" class="form-label" >Expiration Date</label>
        <input type="date" class="form-control" id="inputExpirationDate" v-model="product.expiration_date">
      </div>
      <div class="mb-3 form-check">
        <label for="inputIsActive" class="form-label" >Is Visible</label>
        <input type="checkbox" class="form-check-input" id="inputIsActive" v-model="product.is_visible" required>
      </div>
      <div class="mb-3">
          <label for="inputImage" class="form-label">Image</label>
          <!-- <input type="file" class="form-control" id="inputImage" @input="product.image = $event.target.files[0]" accept="image/png, image/jpeg"> -->
          <input type="file" class="form-control" id="inputImage" accept="image/jpeg" @change="imageUpload" />
      </div>
      <button type="submit" class="btn btn-primary" @click="addProduct"><i class="bi bi-file-plus"></i></button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      product: {
        name: '',
        description: `Product for ${this.$route.params.name}`,
        price: '',
        unit: 'pcs',
        quantity: 1,
        barcode: '',
        is_expired: false,
        expiration_date: '',
        is_available: true,
        is_visible: true,
      },
      selectImage: null,
      units: [
        'kg',
        'g',
        'l',
        'ml',
        'pcs',
        'box',
        'pack',
        'bottle',
      ],
    }
  },
  methods: {
    async addProduct() {
      let fd = new FormData();
      fd.append('image', this.selectImage, this.selectImage.name)
      fd.append('name', this.product.name)
      fd.append('description', this.product.description)
      fd.append('price', this.product.price)
      fd.append('unit', this.product.unit)
      fd.append('quantity', this.product.quantity)
      fd.append('barcode', this.product.barcode)
      fd.append('expiration_date', this.product.expiration_date)
      fd.append('is_visible', this.product.is_visible)
      fd.append('is_available', this.product.is_available)
      this.product.category_id = this.$route.params.id;
      await axios.post(`/product/${this.$route.params.id}/`, fd)
      .then(response => {
        console.log(response);
        if (response.status == 201) {
          alert('Product added');
        } else {
          alert('Product not added');
        }
      }).catch(error => {
        console.log(error);
      });
    },
    imageUpload(event) {
      this.selectImage = event.target.files[0];
    }

  },
}
</script>

<style scoped>
  form {
    margin-bottom: 20px;
  }
</style>
