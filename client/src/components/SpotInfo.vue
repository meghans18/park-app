<template>
    <div id="spotInfo">
        <div class="row">       
            <b-col class="col-6 text-left" style="padding-left: 50px;">
                <p style="color: #0a814c; font-size: 2em;">Spot Information</p>
                <hr>
                <h5><strong>Address:</strong></h5>
                <p> {{spot.addressNum}} {{spot.street}}, {{spot.city}}, {{spot.state}} {{spot.zipcode}} </p>
                <div v-if="spot.spotNumber">
                    <h5><strong>Spot Number:</strong></h5>
                    <p> {{spot.spotNumber}} </p>
                </div>
                <h5><strong>Price Per Day:</strong></h5>
                <p> ${{spot.price}} </p>
                <h5><strong>Date Chosen:</strong></h5>
                <p><em>Not implemented yet</em></p>

                <br>
                <br>

                <b-button variant="danger" style="margin-right: 15px;" @click="$router.push('/')">Back</b-button>
                <b-button variant='success' @click="toCheckout()">Checkout with Stripe</b-button>
            </b-col>
            <b-col class="col-6">
                <google-map :spots="[this.spot]" :center="{ lat: spot.latitude, lng: spot.longitude }"></google-map>
            </b-col>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import GoogleMap from './GoogleMap.vue'

export default {
  components: { GoogleMap },
    name: 'SpotInfo',
    data() {
        return {
            spot: {}
        }
    },
    methods: {
        setSpot(spot_id) {
            const path = `http://localhost:5000/spot/${spot_id}`
            axios.get(path).then((response) => {
                this.spot = response.data.spot
            }).catch((error) => {
                console.error(error);
            });
        },
        toCheckout() {
            var stripe = Stripe('pk_test_51IaQy6CwKcZquRsXh7S1Ep0dnIJhJP0I85FzftkIjhM9zuwqELV8wuHTgRqeWW7Eg2MmXMZ8b47MkSdHuwTXq17a00nbSWxysO'); // eslint-disable-line no-undef
            const payload = {
                userEmail: this.$store.getters.getEmail,
                spotID: this.spot.id,
            }
            const path = 'http://localhost:5000/checkout'
            axios.post(path, payload).then((response) => {
                let session_ID = response.data.session
                stripe.redirectToCheckout({
                    sessionId: session_ID
                }).then(function (result) {
                    console.log(result)
                })
            }).catch((error) => {
                console.error(error)
            })
        }
    },
    created: function() {
        this.setSpot(this.$route.params.spot_id);
    },
}
</script>

<style scoped>

</style>