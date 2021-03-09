<template>
    <div id="leaseSpot" class="container">
        <div class="text-center">
            <p>Manage/Add Spots for Rent</p>
        </div>
        <button type="button" class="btn btn-success btn-md" v-b-modal.spot-modal>Add a New Spot for Rent</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Spot Address</th>
              <th scope="col">List Price</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="spot in spots" :key="spot.id">
              <td>{{spot.addressNum}} {{spot.street}}, {{spot.city}}, {{spot.state}} {{spot.zipcode}}</td>
              <td>${{spot.price}}/per day</td>
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-danger btn-md">Delete Spot</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>


        <b-modal ref="addSpotModal"
                id="spot-modal"
                title="List a New Spot for Rent"
                centered
                hide-footer>
            <b-form @submit="onSubmit" @reset="onReset" class="w-100">
                <b-form-group id="form-addressNum-group"
                            label="Address #:"
                            label-for="form-addressNum-input">
                    <b-form-input id="form-addressNum-input"
                                type="number"
                                v-model="form.addressNum"
                                required
                                placeholder="Enter address number:">
                    </b-form-input>
                </b-form-group>
                <b-form-group id="form-street-group"
                                label="Street:"
                                label-for="form-street-input">
                    <b-form-input id="form-street-input"
                                    type="text"
                                    v-model="form.street"
                                    required
                                    placeholder="Enter street:">
                    </b-form-input>
                </b-form-group>
                <b-form-group id="form-city-group"
                                label="City:"
                                label-for="form-city-input">
                    <b-form-input id="form-city-input"
                                    type="text"
                                    v-model="form.city"
                                    required
                                    placeholder="Enter city:">
                    </b-form-input>
                </b-form-group>
                <b-form-group id="form-state-group"
                                label="State:"
                                label-for="form-state-input">
                    <b-form-input id="form-state-input"
                                    type="text"
                                    v-model="form.state"
                                    required
                                    placeholder="Enter state:">
                    </b-form-input>
                </b-form-group>
                <b-form-group id="form-zipcode-group"
                                label="Zipcode:"
                                label-for="form-zipcode-input">
                    <b-form-input id="form-zipcode-input"
                                    type="number"
                                    v-model="form.zipcode"
                                    required
                                    placeholder="Enter zipcode:">
                    </b-form-input>
                </b-form-group>
                <b-form-group id="form-price-group"
                                label="Price (per day):"
                                label-for="form-price-input">
                    <b-form-input id="form-price-input"
                                    type="number"
                                    v-model="form.price"
                                    required
                                    placeholder="Enter price for the spot per day:">
                    </b-form-input>
                </b-form-group>
                <b-button type="submit" variant="primary">Submit</b-button>
                <b-button type="reset" variant="danger">Reset</b-button>
            </b-form>
        </b-modal>
    </div>
</template>

<script>
export default {
    name: 'LeaseSpot',
    data() {
        return {
            form: {
                addressNum: '',
                street: '',
                city: '',
                state: '',
                zipcode: '',
                price: '',
            },
            spots: [
                {
                    id: 1,
                    addressNum: 1,
                    street: 'Davenport St',
                    city: 'Grundy Center',
                    state: 'Iowa',
                    zipcode: 50613,
                    price: 300
                },
                {
                    id: 2,
                    addressNum: 239,
                    street: 'Rainbow Ave',
                    city: 'Coralville',
                    state: 'Illinois',
                    zipcode: 52245,
                    price: 129
                }
            ],
        }
    },
    methods: {
        onSubmit() {
            //do submit to database stuff here
        },
        onReset() {
            this.form.addressNum = ''
            this.form.street = ''
            this.form.city = ''
            this.form.state = ''
            this.form.zipcode = ''
            this.form.price = ''
        }
    }
}
</script>

<style scoped>
p {
  color: #0a814c;
  font-size: 2em;
}
</style>