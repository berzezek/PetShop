<template>
	<div class="mt-5">
		<br class="mt-5">
		<br class="mt-5">
		<br class="mt-5">
		<br class="mt-5">
		<br class="mt-5">
		<br class="mt-5">
		<h3 class="text-center title">Products</h3>
		<div class="container">
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
					<th scope="col">Options</th>
					</tr>
				</thead>
					<tbody>
						<tr v-for='product in availableProducts' :key="product.id" class="align-middle">
						<th scope="row">{{ product.id }}</th>
						<td>{{ product.name }}</td>
						<td v-if="!product.get_thumbnail"></td>
						<td v-else><img :src="product.get_thumbnail" class="img-rounded" /></td>
						<td>{{ product.price }}</td>
						<td>{{ product.barcode }}</td>
						<td>{{ product.unit }}</td>
						<td>{{ product.quantity }}</td>
						<td>
							<div class="d-flex justify-content-between">

								<router-link
								:to='{ 
									name: "productEdit", 
									params: { 
										id: product.id,
										name: product.name,
										description: product.description,
										price: product.price,
										categoryName: product.category.name,
										categoryId: product.category.id,
										unit: product.unit,
										quantity: product.quantity,
										barcode: product.barcode,
										image: product.get_thumbnail,
										self_price: product.self_price,
										is_expired: product.is_expired,
										expiration_date: product.get_expiration_date,
										is_available: product.is_available,
										is_visible: product.is_visible,
										}}'>

										<div>
											<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pencil" viewBox="0 0 16 16">
												<path d="M12.146.146a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1 0 .708l-10 10a.5.5 0 0 1-.168.11l-5 2a.5.5 0 0 1-.65-.65l2-5a.5.5 0 0 1 .11-.168l10-10zM11.207 2.5 13.5 4.793 14.793 3.5 12.5 1.207 11.207 2.5zm1.586 3L10.5 3.207 4 9.707V10h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.5h.293l6.5-6.5zm-9.761 5.175-.106.106-1.528 3.821 3.821-1.528.106-.106A.5.5 0 0 1 5 12.5V12h-.5a.5.5 0 0 1-.5-.5V11h-.5a.5.5 0 0 1-.468-.325z"/>
											</svg>
										</div>
									</router-link>
									<router-link :to='{ name: "productDelete", params: { id: product.id } }'>
										<div class="text-danger">
											<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-file-x" viewBox="0 0 16 16">
												<path d="M6.146 6.146a.5.5 0 0 1 .708 0L8 7.293l1.146-1.147a.5.5 0 1 1 .708.708L8.707 8l1.147 1.146a.5.5 0 0 1-.708.708L8 8.707 6.854 9.854a.5.5 0 0 1-.708-.708L7.293 8 6.146 6.854a.5.5 0 0 1 0-.708z"/>
												<path d="M4 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H4zm0 1h8a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1z"/>
											</svg>
										</div>
									</router-link>
									<router-link 
									:to='{ 
										name: "productDetail", 
										params: { 
											id: product.id,
											name: product.name,
											description: product.description,
											price: product.price,
											category: product.category.name,
											unit: product.unit,
											quantity: product.quantity,
											barcode: product.barcode,
											image: product.image,
											self_price: product.self_price,
											is_expired: product.is_expired,
											expiration_date: product.expiration_date,
											is_available: product.is_available,
											is_visible: product.is_visible,
											}}'>
										<div class="text-success">
											<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-three-dots-vertical" viewBox="0 0 16 16">
											<path d="M9.5 13a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0zm0-5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0zm0-5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0z"/>
											</svg>
										</div>
									</router-link>
								</div>
							</td>
						</tr>
					</tbody>
				</table>
			</div>

    </div>

</template>

<script>
import axios from 'axios';
import ProductAdd from '@/components/product/ProductAdd.vue';
export default {
	components: {
		ProductAdd
	},
	data() {
		return {
			products: [],
			availableProducts: []
		}
	},
	methods: {

		async getProducts() {
			await axios.get('products/')
				.then(response => {

					this.products = response.data;
					this.filterByAvailable()
					console.log(this.availableProducts);
			})
				.catch(error => {
					console.log(error)
			})
		},
		filterByAvailable() {
			this.products.forEach(product => {
				if (product.is_available === true) {
					this.availableProducts.push(product);
				}
			})
		},
	},
	mounted() {
		this.getProducts()
		
		// console.log(this.availableProducts)
	},
}
</script>

<style scoped>
	img {
		width: 45px;
		height: 45px;
	}
</style>