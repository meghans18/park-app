<template>
    <div id="rented-spots" class="container">
        <div class="text-center">
            <p style="color: #0a814c; font-size: 2em;">Your Current Reservations</p>
            <table class="table table-hover">
                <thead>
                    <tr>
                    <th scope="col">Spot Address</th>
                    <th scope="col">Spot Number</th>
                    <th scope="col">Spot Price</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="reservation in reservations" :key="reservation.reservationNum">
                    <td>{{reservation.addressNum}} {{reservation.street}}, {{reservation.city}}, {{reservation.state}} {{reservation.zipcode}}</td>
                    <td>{{reservation.spotNumber}}</td>
                    <td>${{reservation.price}}/per day</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'RentedSpots',
    data() {
        return {
            reservations: {}
        }
    },
    methods: {
        getReservations() {
            let userEmail = this.$store.getters.getEmail
            const path = `http://localhost:5000/reservations/${userEmail}`
            axios.get(path).then((response) => {
                this.reservations = response.data.reservations
            })
        }
    },
    mounted: function() {
        this.getReservations();
    }
}
</script>