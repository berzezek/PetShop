<template>
	<div class="">
		<h3 class="text-center title">Products</h3>
		<div class="container" >
			<table class="table table-striped">
				<thead>
						<tr>
						<th scope="col">#</th>
						<th scope="col">Title</th>
						<th scope="col">Image</th>
						<th scope="col">Price</th>
						<th scope="col">Barcode</th>
						<th scope="col">Unit</th>
						<th scope="col">Qty</th>
						</tr>
				</thead>
					<tbody>
						<tr v-for='product in products' :key="product.id" v-show="product.is_available" class="align-middle" @click="addProductToOrder(product.id)">
							<th scope="row">{{ product.id }}</th>
							<td>{{ product.name }}</td>
							<td v-if="!product.get_thumbnail"></td>
							<td v-else><img :src="product.get_thumbnail" class="img-rounded" /></td>
							<td>{{ product.price }}</td>
							<td>{{ product.barcode }}</td>
							<td>{{ product.unit }}</td>
							<td>{{ product.quantity }}</td>
						</tr>
					</tbody>
				</table>
			</div>

    </div>

</template>

<script>
import axios from 'axios';
export default {
	name: 'order-product',

	data() {
			return {
					products: [],
			}
	},
	methods: {
		async getProducts() {
			await axios.get('products/')
				.then(response => {
					this.products = response.data;
				})
				.catch(error => {
					console.log(error)
				})
		},
		addProductToOrder(id) {
			let fd = new FormData();
			fd.append('product_id', id);
			fd.append('order_id', this.$route.params.id);
			fd.append('quantity', 1);
			for (var pair of fd.entries()) {
				console.log(pair[0]+ ', '+ pair[1]);
			}
		},
	},
	mounted() {
			this.getProducts()
	},
}
</script>

<style scoped>
	img {
			width: 45px;
			height: 45px;
	}
</style>